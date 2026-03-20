# 🎓 Student Manager — Flask + MongoDB Minor Project

A full-stack web application to manage student records built with **Flask**, **PyMongo**, and **MongoDB**.

---

## 📁 Project Structure

```
student_manager/
├── app.py                  # Flask app & REST API routes
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Frontend (HTML + CSS + JS)
└── README.md
```

---

## ⚙️ Setup & Run

### 1. Install MongoDB
Make sure MongoDB is running locally on port `27017`.
- Download: https://www.mongodb.com/try/download/community

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux / Mac
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```

Open your browser at: **http://localhost:5000**

---

## 🔗 REST API Endpoints

| Method | Endpoint                  | Description              |
|--------|---------------------------|--------------------------|
| GET    | `/api/students`           | List all students        |
| GET    | `/api/students?search=x`  | Search by name / email   |
| GET    | `/api/students?dept=CS`   | Filter by department     |
| POST   | `/api/students`           | Create a student         |
| GET    | `/api/students/<id>`      | Get one student by ID    |
| PUT    | `/api/students/<id>`      | Update student details   |
| DELETE | `/api/students/<id>`      | Delete a student         |
| GET    | `/api/stats`              | Dashboard statistics     |

### POST body example (`/api/students`):
```json
{
  "name":       "Priya Sharma",
  "email":      "priya@college.edu",
  "age":        21,
  "department": "Computer Science",
  "grade":      "A+"
}
```

---

## 🛠️ Tech Stack

| Layer     | Technology         |
|-----------|--------------------|
| Backend   | Python 3, Flask    |
| Database  | MongoDB (NoSQL)    |
| ODM       | PyMongo            |
| Frontend  | HTML5, CSS3, JS    |
| Routes    | Flask path routing |

---

## 🌿 Environment Variables

| Variable    | Default                      | Description         |
|-------------|------------------------------|---------------------|
| `MONGO_URI` | `mongodb://localhost:27017/` | MongoDB connection  |

Set a custom URI:
```bash
export MONGO_URI="mongodb+srv://user:pass@cluster.mongodb.net/"
```

---

## ✨ Features

- ✅ Full CRUD for student records
- ✅ Search by name / email
- ✅ Filter by department
- ✅ Dashboard stats (total, departments, avg age)
- ✅ Duplicate email detection
- ✅ Clean dark-themed UI with toast notifications
