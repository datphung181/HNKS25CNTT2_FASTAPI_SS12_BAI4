from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Student
 
def delete_student_service(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Học viên không tồn tại trong hệ thống")
    student_data = {"id": student.id, "full_name": student.full_name, "email": student.email}
    db.delete(student)
    db.commit()
    return student_data
 