from pydantic import BaseModel
from datetime import datetime

class ContactBase(BaseModel):
    first_name: str 
    last_name: str 
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
    gross_pay: int
    payroll_deductions: int
    Reason: str

class AddSalary(SalaryBase):
    pass

class Salary(SalaryBase):
    id: int
    owner_id: int
    time: datetime

    class Config:
        orm_mode = True
