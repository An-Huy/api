from pydantic import BaseModel
from datetime import datetime

class ContactBase(BaseModel):
    first_name: str 
    last_name: str 
    sex: str
    email: str
    phone_number: str

class AddContact(ContactBase):
    pass

class Contact(ContactBase):
    id: int
    time: datetime
    
    class Config:
        orm_mode = True

class SalaryBase(BaseModel):
    note: str
    salary: int

class AddSalary(SalaryBase):
    pass

class Salary(SalaryBase):
    id: int
    employee_id: int
    time: datetime

    class Config:
        orm_mode = True