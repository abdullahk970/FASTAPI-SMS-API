from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import models
import schemas
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="School REST API", version="1.0")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/departments", response_model=schemas.DepartmentOut)
def create_department(payload: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    exists = db.query(models.Department).filter(models.Department.name == payload.name).first()
    if exists:
        raise HTTPException(status_code=400, detail="Department with this name already exists")
    return crud.create_department(db, name=payload.name)

@app.get("/departments", response_model=list[schemas.DepartmentOut])
def list_departments(db: Session = Depends(get_db)):
    return db.query(models.Department).all()

@app.post("/teachers", response_model=schemas.TeacherOut)
def create_teacher(payload: schemas.TeacherCreate, db: Session = Depends(get_db)):
    return crud.create_teacher(db, name=payload.name)

@app.get("/departments", response_model=list[schemas.DepartmentOut])
def list_departments(db: Session = Depends(get_db)):
    return db.query(models.Department).all()

@app.post("/teachers", response_model=schemas.TeacherOut)
def create_teacher(payload: schemas.TeacherCreate, db: Session = Depends(get_db)):
    return crud.create_teacher(db, name=payload.name)

@app.get("/teachers", response_model=list[schemas.TeacherOut])
def list_teachers(db: Session = Depends(get_db)):
    return db.query(models.Teacher).all()

@app.post("/courses", response_model=schemas.CourseOut)
def create_course(payload: schemas.CourseCreate, db: Session = Depends(get_db)):
    dept = db.query(models.Department).filter(models.Department.id == payload.department_id).first()
    if not dept:
        raise HTTPException(status_code=404, detail="Department not found")
    teacher = None
    if payload.teacher_id is not None:
        teacher = db.query(models.Teacher).filter(models.Teacher.id == payload.teacher_id).first()
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
    return crud.create_course(db, title=payload.title, department_id=payload.department_id, teacher_id=payload.teacher_id)

@app.get("/courses", response_model=list[schemas.CourseOut])
def list_courses(db: Session = Depends(get_db)):
    return db.query(models.Course).all()

@app.post("/students", response_model=schemas.StudentOut)
def create_student(payload: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, name=payload.name)

@app.get("/students", response_model=list[schemas.StudentOut])
def list_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

@app.post("/enrollments")
def enroll(payload: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == payload.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    course = db.query(models.Course).filter(models.Course.id == payload.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    e = crud.enroll_student(db, student_id=payload.student_id, course_id=payload.course_id, grade=payload.grade)
    return {"message": "Enrollment saved", "student_id": e.student_id, "course_id": e.course_id, "grade": e.grade}

@app.get("/students/{student_id}/courses", response_model=list[schemas.StudentCourseItem])
def student_courses(student_id: int, db: Session = Depends(get_db)):
    exists = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not exists:
        raise HTTPException(status_code=404, detail="Student not found")
    rows = (
        db.query(models.Enrollment, models.Course)
        .join(models.Course, models.Enrollment.course_id == models.Course.id)
        .filter(models.Enrollment.student_id == student_id)
        .all()
    )
    return [
        {"course_id": c.id, "title": c.title, "grade": e.grade}
        for (e, c) in rows
    ]

@app.get("/courses/{course_id}/students", response_model=list[schemas.CourseStudentItem])
def course_students(course_id: int, db: Session = Depends(get_db)):
    exists = db.query(models.Course).filter