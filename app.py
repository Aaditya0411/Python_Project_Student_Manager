from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId
from bson.errors import InvalidId
import os
from datetime import datetime

app = Flask(__name__)


MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
client     = MongoClient(MONGO_URI)
db         = client["student_db"]
students   = db["students"]


def serialize(doc):
    doc["_id"] = str(doc["_id"])
    return doc


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/api/students", methods=["GET"])
def get_students():
    query  = {}
    search = request.args.get("search", "").strip()
    dept   = request.args.get("dept", "").strip()

    if search:
        query["$or"] = [
            {"name":  {"$regex": search, "$options": "i"}},
            {"email": {"$regex": search, "$options": "i"}},
        ]
    if dept:
        query["department"] = {"$regex": dept, "$options": "i"}

    docs = [serialize(s) for s in students.find(query).sort("name", 1)]
    return jsonify(docs)



@app.route("/api/students", methods=["POST"])
def create_student():
    data = request.json or {}
    required = ["name", "email", "age", "department"]
    missing  = [f for f in required if not data.get(f)]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    if students.find_one({"email": data["email"]}):
        return jsonify({"error": "Email already registered"}), 409

    doc = {
        "name":       data["name"].strip(),
        "email":      data["email"].strip().lower(),
        "age":        int(data["age"]),
        "department": data["department"].strip(),
        "grade":      data.get("grade", "N/A"),
        "created_at": datetime.utcnow().isoformat(),
    }
    result = students.insert_one(doc)
    doc["_id"] = str(result.inserted_id)
    return jsonify(doc), 201



@app.route("/api/students/<sid>", methods=["GET"])
def get_student(sid):
    try:
        doc = students.find_one({"_id": ObjectId(sid)})
    except InvalidId:
        return jsonify({"error": "Invalid ID"}), 400
    if not doc:
        return jsonify({"error": "Not found"}), 404
    return jsonify(serialize(doc))



@app.route("/api/students/<sid>", methods=["PUT"])
def update_student(sid):
    try:
        oid = ObjectId(sid)
    except InvalidId:
        return jsonify({"error": "Invalid ID"}), 400

    data = request.json or {}
    allowed = ["name", "email", "age", "department", "grade"]
    update  = {k: v for k, v in data.items() if k in allowed and v != ""}

    if "age" in update:
        update["age"] = int(update["age"])

    if not update:
        return jsonify({"error": "No valid fields provided"}), 400

    res = students.update_one({"_id": oid}, {"$set": update})
    if res.matched_count == 0:
        return jsonify({"error": "Not found"}), 404

    updated = serialize(students.find_one({"_id": oid}))
    return jsonify(updated)


@app.route("/api/students/<sid>", methods=["DELETE"])
def delete_student(sid):
    try:
        oid = ObjectId(sid)
    except InvalidId:
        return jsonify({"error": "Invalid ID"}), 400

    res = students.delete_one({"_id": oid})
    if res.deleted_count == 0:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"message": "Student deleted successfully"})



@app.route("/api/stats", methods=["GET"])
def stats():
    total = students.count_documents({})
    depts = students.distinct("department")
    avg_age_pipeline = [{"$group": {"_id": None, "avg": {"$avg": "$age"}}}]
    avg_result = list(students.aggregate(avg_age_pipeline))
    avg_age = round(avg_result[0]["avg"], 1) if avg_result else 0

    dept_counts = list(students.aggregate([
        {"$group": {"_id": "$department", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]))

    return jsonify({
        "total":      total,
        "departments": len(depts),
        "avg_age":    avg_age,
        "dept_breakdown": dept_counts,
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
