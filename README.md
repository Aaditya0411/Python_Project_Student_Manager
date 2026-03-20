# 🎓 Student Manager — Flask + MongoDB

A full-stack **Student Record Management System** built with Python Flask, MongoDB, and a modern dark-themed UI. Perform full CRUD operations, search/filter students, and view live dashboard statistics.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.3-black?style=flat-square&logo=flask)
![MongoDB](https://img.shields.io/badge/MongoDB-4.7.2-green?style=flat-square&logo=mongodb)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 📸 Features

- ✅ Add, Edit, Delete student records
- ✅ Search students by name or email
- ✅ Filter students by department
- ✅ Live dashboard stats (total students, departments, average age)
- ✅ Duplicate email detection
- ✅ Toast notifications for all actions
- ✅ Fully responsive dark UI

---

## 📁 Project Structure

```
StudentManager/
├── app.py                  # Flask backend & REST API
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Frontend (HTML + CSS + Vanilla JS)
└── README.md
```

---

## 🛠️ Tech Stack

| Layer      | Technology              |
|------------|-------------------------|
| Backend    | Python 3, Flask 3.0     |
| Database   | MongoDB (NoSQL)         |
| Driver     | PyMongo 4.7             |
| Frontend   | HTML5, CSS3, JavaScript |
| Routing    | Flask path routing      |

---

## ⚙️ Installation & Setup

### Prerequisites

Make sure you have the following installed:

- ✅ [Python 3.10+](https://www.python.org/downloads/)
- ✅ [MongoDB Community Server](https://www.mongodb.com/try/download/community)
- ✅ [Git](https://git-scm.com/downloads)

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/Aaditya0411/Python_Project_Student_Manager.git
cd Python_Project_Student_Manager
```

---

### Step 2 — Create a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

> ✅ You'll see `(venv)` appear at the start of your terminal line when activated.

---

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `flask==3.0.3`
- `pymongo==4.7.2`

---

### Step 4 — Start MongoDB

Make sure MongoDB is running on your machine before starting the app.

**Windows:**
```powershell
net start MongoDB
```

**Mac / Linux:**
```bash
sudo systemctl start mongod
# or
brew services start mongodb-community
```

> MongoDB runs on `localhost:27017` by default. The app connects to it automatically.

---

### Step 5 — Run the Application

```bash
python app.py
```

You should see:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

Open your browser and go to 👉 **http://127.0.0.1:5000**

---

## 🔗 REST API Reference

Base URL: `http://127.0.0.1:5000`

### Get All Students
```http
GET /api/students
```

**Query Parameters (optional):**

| Parameter | Type   | Description                    |
|-----------|--------|--------------------------------|
| `search`  | string | Search by name or email        |
| `dept`    | string | Filter by department name      |

**Example:**
```
GET /api/students?search=priya&dept=Computer Science
```

---

### Get Single Student
```http
GET /api/students/<id>
```

---

### Create Student
```http
POST /api/students
Content-Type: application/json
```

**Request Body:**
```json
{
  "name":       "Priya Sharma",
  "email":      "priya@college.edu",
  "age":        21,
  "department": "Computer Science",
  "grade":      "A+"
}
```

**Response `201`:**
```json
{
  "_id":        "665f1a2b3c4d5e6f7a8b9c0d",
  "name":       "Priya Sharma",
  "email":      "priya@college.edu",
  "age":        21,
  "department": "Computer Science",
  "grade":      "A+",
  "created_at": "2025-01-01T10:00:00"
}
```

---

### Update Student
```http
PUT /api/students/<id>
Content-Type: application/json
```

**Request Body (any updatable fields):**
```json
{
  "grade": "A",
  "age": 22
}
```

---

### Delete Student
```http
DELETE /api/students/<id>
```

**Response `200`:**
```json
{ "message": "Student deleted successfully" }
```

---

### Dashboard Stats
```http
GET /api/stats
```

**Response:**
```json
{
  "total":      42,
  "departments": 5,
  "avg_age":    20.8,
  "dept_breakdown": [
    { "_id": "Computer Science", "count": 15 },
    { "_id": "Electronics",      "count": 10 }
  ]
}
```

---

## 🌿 Environment Variables

You can override the default MongoDB URI using an environment variable:

**Windows (PowerShell):**
```powershell
$env:MONGO_URI = "mongodb+srv://user:password@cluster.mongodb.net/"
python app.py
```

**Mac / Linux:**
```bash
export MONGO_URI="mongodb+srv://user:password@cluster.mongodb.net/"
python app.py
```

| Variable    | Default                      | Description              |
|-------------|------------------------------|--------------------------|
| `MONGO_URI` | `mongodb://localhost:27017/` | MongoDB connection string |

---

## ❗ Common Errors & Fixes

### `WinError 10038` on Windows
```bash
# Fix: use_reloader=False is already set in app.py
app.run(debug=True, port=5000, use_reloader=False)
```

### `source` not recognized in PowerShell
```powershell
# Wrong ❌
source venv/bin/activate

# Correct ✅
venv\Scripts\activate
```

### PowerShell script execution blocked
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### MongoDB connection refused
Make sure MongoDB service is running:
```powershell
net start MongoDB     # Windows
```

---

## 🔄 Git Commands (Quick Reference)

```bash
# Clone
git clone https://github.com/Aaditya0411/Python_Project_Student_Manager.git

# After making changes
git add .
git commit -m "describe your change"
git push

# Check status
git status

# View history
git log --oneline
```

---

## 📄 License

This project is licensed under the **MIT License** — free to use and modify.

---

## 👤 Author

**Aaditya**  
GitHub: [@Aaditya0411](https://github.com/Aaditya0411)

---

> 💡 **Tip:** Use [MongoDB Compass](https://www.mongodb.com/products/compass) (free GUI tool) to visually browse your `student_db` database while the app is running.
