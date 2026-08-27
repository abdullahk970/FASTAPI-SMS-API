from typing import Optional

from pydantic import BaseModel

class DepartmentCreate(BaseModel):
name: str

class DepartmentOut(BaseModel):
id: int
name: str

```
class Config:
    from_attributes = True
```

class TeacherCreate(BaseModel):
name: str

class TeacherOut(BaseModel):
id: int
name: str

```
class Config:
    from_attributes = True
```

class CourseCreate(BaseModel):
title: str
department_id: int
teacher_id: Optional[int] = None

class CourseOut(BaseModel):
id: int
title: str
department: DepartmentOut
teacher: Optional[TeacherOut] = None

class StudentCreate(BaseModel):
name: str

class StudentOut(BaseModel):
id: int
name: str

```
class Config:
    from_attributes = True
```

class EnrollmentCreate(BaseModel):
student_id: int
course_id: int
grade: Optional[str] = None

class StudentCourseItem(BaseModel):
course_id: int
title: str
grade: Optional[str] = None

class CourseStudentItem(BaseModel):
student_id: int
name: str
grade: Optional[str] = None
