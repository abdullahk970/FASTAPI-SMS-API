# ⚡ FastAPI School Management API

> A RESTful school management API built with FastAPI, SQLAlchemy, and Pydantic, demonstrating relational database modeling, CRUD operations, validation, and entity relationships.

![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![Python](https://img.shields.io/badge/Python-3.10+-blue)

---

## 📌 Overview

This project is a backend API for managing core school entities and their relationships.

The application demonstrates how a FastAPI service can use SQLAlchemy ORM models and Pydantic schemas to expose structured CRUD operations over a relational database.

The main entities are:

* Students
* Teachers
* Departments
* Courses
* Enrollments

---

## 🎯 What This Project Demonstrates

This project focuses on backend engineering fundamentals, including:

* REST API development
* CRUD operations
* SQLAlchemy ORM
* Pydantic validation
* Relational database modeling
* One-to-many relationships
* Many-to-many relationships
* Dependency-based database sessions
* API documentation through FastAPI

---

## ✨ Key Features

* Full CRUD operations for core school entities
* Student and course enrollment management
* Duplicate enrollment prevention
* ORM-based database queries
* Request and response validation
* Interactive Swagger API documentation

---

## 🏗️ Data Model

The application contains the following relationships:

```text
Department
    │
    └──────────< Course
                   │
                   ├── Teacher
                   │
                   └──< Enrollment >── Student
```

### Relationships

**Department → Course**

One department can contain multiple courses.

**Student ↔ Course**

Students and courses have a many-to-many relationship through the `Enrollment` table.

**Teacher → Course**

A teacher can be associated with courses through the course model.

---

## 📦 Data Models

| Model      | Main Fields                          |
| ---------- | ------------------------------------ |
| Student    | id, name                             |
| Teacher    | id, name                             |
| Department | id, name                             |
| Course     | id, title, department_id, teacher_id |
| Enrollment | student_id, course_id, grade         |

---

## 🛠️ Tech Stack

| Layer         | Technology |
| ------------- | ---------- |
| Language      | Python     |
| API Framework | FastAPI    |
| ORM           | SQLAlchemy |
| Validation    | Pydantic   |
| Database      | SQLite     |
| ASGI Server   | Uvicorn    |

---

## 📂 Project Structure

```text
FASTAPI-SMS-API/
│
├── database.py
│   └── Database engine and session configuration
│
├── models.py
│   └── SQLAlchemy ORM models
│
├── schemas.py
│   └── Pydantic request/response schemas
│
├── crud.py
│   └── Database operations
│
├── main.py
│   └── FastAPI application entry point
│
├── demo.py
│   └── Example/demo usage
│
└── README.md
```

---

## ⚙️ Getting Started

### Prerequisites

Install:

* Python 3.10+
* Git

---

### 1. Clone the Repository

```bash
git clone https://github.com/abdullahk970/FASTAPI-SMS-API.git

cd FASTAPI-SMS-API
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

---

### 4. Start the API

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI's interactive documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

## 🔌 API

The API provides CRUD functionality for the application's main entities.

Typical resource groups include:

* Students
* Teachers
* Departments
* Courses
* Enrollments

Use the automatically generated Swagger documentation at `/docs` to inspect the currently available routes, request schemas, and response models.

---

## 🧠 Example: Preventing Duplicate Enrollment

The enrollment logic checks whether the same student is already enrolled in the same course before creating another record.

Example:

```python
already = db.query(Enrollment).filter(
    Enrollment.student_id == student_id,
    Enrollment.course_id == course_id
).first()

if already:
    return already
```

This demonstrates application-level validation for relationship data.

---

## 🔐 Security Considerations

The current project is primarily a backend learning/project implementation.

For production use, additional controls would be required, including:

* authentication and authorization
* role-based access control
* stronger input validation
* rate limiting
* production database configuration
* secure secret management
* structured error handling
* automated testing

---

## 🧪 Testing

Automated test coverage is a potential area for future development.

A production-oriented version should include tests for:

* CRUD operations
* validation failures
* relationship handling
* duplicate enrollment behavior
* API error responses

No test coverage percentage is claimed here because a complete automated test suite is not currently documented.

---

## 🔮 Future Improvements

Potential improvements include:

* JWT authentication
* Role-based access control
* Pagination and filtering
* Automated Pytest coverage
* Docker support
* PostgreSQL support
* Improved API error handling
* Production deployment configuration

---

## ⚠️ Limitations

* The current project uses SQLite for local database storage.
* Authentication and authorization are not the primary focus of the current implementation.
* Automated testing can be expanded.
* The project is primarily intended to demonstrate backend and database fundamentals.

---

## 👨‍💻 Author

**Muhammad Abdullah Khan**

* GitHub: [abdullahk970](https://github.com/abdullahk970)
* LinkedIn: [Muhammad Abdullah Khan](https://www.linkedin.com/in/muhammad-abdullah-khan-9b0980316?utm_source=share_via&utm_content=profile&utm_medium=member_android)

---

## 📄 License

This project is licensed under the MIT License.
