# ⚡ FastAPI CRUD + SQLAlchemy School Management System

> A production-structured **FastAPI CRUD application** demonstrating relational database design using **SQLAlchemy ORM**, **Pydantic schemas**, and a clean layered architecture for managing students, courses, teachers, departments, and enrollments.

![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 🚀 Overview

This project is a **School Management CRUD API** built using FastAPI and SQLAlchemy. It demonstrates how to design and implement **relational database models** with proper relationships such as:

* One-to-Many (Department → Courses)
* Many-to-Many (Students ↔ Courses via Enrollments)
* Optional relationships (Teacher → Courses)

The project is structured for **real-world backend development**, focusing on scalability, clean code separation, and database normalization.

---

# 🧠 Key Features

### 📚 Core Entities

* Students
* Teachers
* Departments
* Courses
* Enrollments (junction table)

### 🔗 Relationships

* Students can enroll in multiple courses
* Courses belong to departments
* Courses can be assigned to teachers
* Enrollments store grades

### ⚙️ Backend Features

* Full CRUD operations
* Duplicate enrollment prevention
* ORM-based relational queries
* Pydantic validation layer
* Clean service-based architecture

---

# 🏗️ Tech Stack

* ⚡ FastAPI (Backend Framework)
* 🗄️ SQLAlchemy (ORM)
* 🐍 Python 3.10+
* 🗃️ SQLite (Database)
* 📦 Pydantic (Schema Validation)
* 🔄 Uvicorn (ASGI Server)

---

# 🗂️ Project Structure

```text id="fastapi-structure"
app/
│
├── database.py        # DB engine & session setup
├── models.py          # SQLAlchemy ORM models
├── schemas.py         # Pydantic schemas
├── crud.py            # Database operations (business logic)
├── main.py            # FastAPI entry point
```

---

# 🗄️ Database Setup

### Engine Configuration

```python id="db-engine"
SQLALCHEMY_DATABASE_URL = "sqlite:///./school.db"
```

* Local SQLite database
* Thread-safe configuration enabled

### Session Management

* `SessionLocal` handles DB sessions
* `Base` is declarative ORM base class

---

# 📦 Database Models

### 👨‍🎓 Student

* id
* name
* enrollments (relationship)

### 👩‍🏫 Teacher

* id
* name
* courses

### 🏢 Department

* id
* name
* courses

### 📘 Course

* id
* title
* department_id
* teacher_id

### 🔗 Enrollment (Many-to-Many)

* student_id
* course_id
* grade

---

# 🔄 Relationships Overview

```text id="relations"
Student ↔ Enrollment ↔ Course
Course → Department
Course → Teacher
```

* Many-to-many via `Enrollment`
* One-to-many via `Department → Course`
* Optional relationship via `Teacher`

---

# ⚙️ CRUD Operations

### 🏢 Department

* Create department

### 👩‍🏫 Teacher

* Create teacher

### 📘 Course

* Create course (linked with department & teacher)

### 👨‍🎓 Student

* Create student

### 🔗 Enrollment

* Enroll student in course
* Prevent duplicate enrollments
* Optional grade assignment

---

# 🧠 Business Logic (CRUD Layer)

Example: Prevent duplicate enrollment

```python id="enroll-logic"
already = db.query(Enrollment).filter(
    Enrollment.student_id == student_id,
    Enrollment.course_id == course_id
).first()

if already:
    return already
```

---

# 📊 Pydantic Schemas

### Key Features

* Request validation
* Response serialization
* ORM compatibility (`from_attributes=True`)

### Example Schemas

* DepartmentCreate / DepartmentOut
* StudentCreate / StudentOut
* CourseCreate / CourseOut
* EnrollmentCreate

---

# 🚀 Installation

## Clone Repository

```bash id="clone-fastapi"
git clone https://github.com/yourusername/fastapi-crud-school.git

cd fastapi-crud-school
```

---

## Create Virtual Environment

```bash id="venv-fastapi"
python -m venv venv
```

Activate:

**Windows**

```bash id="activate-win"
venv\Scripts\activate
```

**Linux / Mac**

```bash id="activate-linux"
source venv/bin/activate
```

---

## Install Dependencies

```bash id="install-fastapi"
pip install fastapi uvicorn sqlalchemy pydantic
```

---

## Run Server

```bash id="run-fastapi"
uvicorn main:app --reload
```

Server runs at:

```text id="url-fastapi"
http://127.0.0.1:8000
```

---

# 📡 API Features (Expected Endpoints)

### Students

* POST /students
* GET /students

### Teachers

* POST /teachers

### Courses

* POST /courses
* GET /courses

### Departments

* POST /departments

### Enrollments

* POST /enroll

---

# 🧪 Example Use Case

### Create Department

```json id="dept-json"
{ "name": "Computer Science" }
```

### Create Student

```json id="student-json"
{ "name": "Ali Khan" }
```

### Enroll Student

```json id="enroll-json"
{
  "student_id": 1,
  "course_id": 2,
  "grade": "A"
}
```

---

# 📈 Key Highlights

* Clean layered architecture (DB → CRUD → API)
* Proper ORM relationships
* Many-to-many implementation
* Duplicate-safe enrollment logic
* Scalable school management design
* Production-style structure

---

# 🔮 Future Improvements

* 🔐 JWT Authentication (Admin / Student roles)
* 📊 Admin Dashboard (Analytics)
* 📄 Pagination + Filtering APIs
* 🧪 Pytest Unit Testing
* 🐳 Docker Support
* ☁️ Cloud Deployment (Render / AWS)
* 📘 Swagger Documentation Enhancements

---

# 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push branch
5. Open Pull Request

---

# 👨‍💻 Author

**Muhammad Abdullah Khan**


## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
