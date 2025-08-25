from sqlalchemy.orm import Session
import models

def create_department(db: Session, name: str) -> models.Department:
    dept = models.Department(name=name)
    db.add(dept)
    db.commit()
    db.refresh(dept)
    return dept

def create_teacher(db: Session, name: str) -> models.Teacher:
    t = models.Teacher(name=name)
    db.add(t)
    db.commit()
    db.refresh(t)
    return t

def create_course(db: Session, title: str, department_id: int, teacher_id: int | None) -> models.Course:
    course = models.Course(title=title, department_id=department_id, teacher_id=teacher_id)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

def create_student(db: Session, name: str) -> models.Student:
    s = models.Student(name=name)
    db.add(s)
    db.commit()
    db.refresh(s)
    return s

def enroll_student(db: Session, student_id: int, course_id: int, grade: str | None):
    already = (
        db.query(models.Enrollment)
        .filter(models.Enrollment.student_id == student_id,
        models.Enrollment.course_id == course_id)
        .first()
    )
    if already:
        return already
    e = models.Enrollment(student_id=student_id, course_id=course_id, grade=grade)
    db.add(e)
    db.commit()
    db.refresh(e)
    return e