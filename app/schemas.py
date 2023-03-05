from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ContactBase(BaseModel):
    name: str 
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
    owner_id: int
    time: datetime

    class Config:
        orm_mode = True