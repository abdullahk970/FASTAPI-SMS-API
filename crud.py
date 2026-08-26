from sqlalchemy.orm import Session

import models

def create_department(db: Session, name: str) -> models.Department:
department = models.Department(name=name)
db.add(department)
db.commit()
db.refresh(department)
return department

def create_teacher(db: Session, name: str) -> models.Teacher:
teacher = models.Teacher(name=name)
db.add(teacher)
db.commit()
db.refresh(teacher)
return teacher

def create_course(
db: Session,
title: str,
department_id: int,
teacher_id: int | None,
) -> models.Course:
course = models.Course(
title=title,
department_id=department_id,
teacher_id=teacher_id,
)
db.add(course)
db.commit()
db.refresh(course)
return course

def create_student(db: Session, name: str) -> models.Student:
student = models.Student(name=name)
db.add(student)
db.commit()
db.refresh(student)
return student

def enroll_student(
db: Session,
student_id: int,
course_id: int,
grade: str | None,
) -> models.Enrollment:
existing_enrollment = (
db.query(models.Enrollment)
.filter(
models.Enrollment.student_id == student_id,
models.Enrollment.course_id == course_id,
)
.first()
)

```
if existing_enrollment:
    return existing_enrollment

enrollment = models.Enrollment(
    student_id=student_id,
    course_id=course_id,
    grade=grade,
)

db.add(enrollment)
db.commit()
db.refresh(enrollment)

return enrollment
```
