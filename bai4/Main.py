from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, engine, Base
from Services import delete_student_service
from schemas import DeleteStudentResponse
 
Base.metadata.create_all(bind=engine)
app = FastAPI()
 
@app.delete("/students/{student_id}", response_model=DeleteStudentResponse)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student_data = delete_student_service(db, student_id)
    return {"message": "Xóa học viên thành công", "data": student_data}
 