# ⚡ FastAPI School Management System (CRUD + SQLAlchemy)

> A FastAPI CRUD application demonstrating relational database design with SQLAlchemy ORM and Pydantic validation — managing students, teachers, departments, courses, and enrollments.

![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red) ![SQLite](https://img.shields.io/badge/Database-SQLite-blue) ![Python](https://img.shields.io/badge/Python-3.10+-blue)

---

## ⚠️ Before you push this

Your repo currently has `__pycache__/` and `school.db` committed directly to git. Fix this first:

```bash
# Remove them from git tracking (keeps local files, removes from repo)
git rm -r --cached __pycache__
git rm --cached school.db

# Add a .gitignore
echo "__pycache__/
*.db
*.pyc" > .gitignore

git add .gitignore
git commit -m "Add .gitignore, remove cache and db from tracking"
git push
```

Committing cache files and a live database is a common backend hygiene mistake — this two-minute fix makes the repo look meaningfully more professional.

---

## 🚀 Overview

This project implements a School Management CRUD API demonstrating proper relational database modeling:

- **One-to-Many**: Department → Courses
- **Many-to-Many**: Students ↔ Courses (via an Enrollment junction table)
- **Optional relationship**: Teacher → Courses

## ✨ Key Features

- Full CRUD operations across five entities (Students, Teachers, Departments, Courses, Enrollments)
- Duplicate enrollment prevention
- ORM-based relational queries
- Pydantic request/response validation

## 🏗️ Tech Stack

- FastAPI (backend framework)
- SQLAlchemy (ORM)
- Python 3.10+
- SQLite (database)
- Pydantic (schema validation)
- Uvicorn (ASGI server)

## 📂 Project Structure

```
FASTAPI-SMS-API/
│
├── database.py     # DB engine & session setup
├── models.py       # SQLAlchemy ORM models
├── schemas.py       # Pydantic schemas
├── crud.py          # Database operations (business logic)
├── main.py          # FastAPI entry point
├── demo.py          # Example/demo usage script
└── README.md
```

## ⚙️ Installation

```bash
git clone https://github.com/abdullahk970/FASTAPI-SMS-API.git
cd FASTAPI-SMS-API

python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

pip install fastapi uvicorn sqlalchemy pydantic

uvicorn main:app --reload
```

Server runs at `http://127.0.0.1:8000` — interactive docs available at `http://127.0.0.1:8000/docs`.

## 📦 Data Models

| Model | Key Fields |
|---|---|
| Student | id, name, enrollments (relationship) |
| Teacher | id, name, courses |
| Department | id, name, courses |
| Course | id, title, department_id, teacher_id |
| Enrollment | student_id, course_id, grade |

## 🧠 Example: Duplicate-Safe Enrollment

```python
already = db.query(Enrollment).filter(
    Enrollment.student_id == student_id,
    Enrollment.course_id == course_id
).first()

if already:
    return already
```

## 🔮 Possible Future Improvements

- JWT authentication (admin/student roles)
- Pagination and filtering on list endpoints
- Pytest unit test coverage
- Docker support

## 👨‍💻 Author

**Muhammad Abdullah Khan**
