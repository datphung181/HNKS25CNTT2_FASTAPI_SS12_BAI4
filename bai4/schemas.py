from pydantic import BaseModel
 
class StudentResponse(BaseModel):
    id: int
    full_name: str
    email: str
    class Config:
        from_attributes = True
 
class DeleteStudentResponse(BaseModel):
    message: str
    data: StudentResponse