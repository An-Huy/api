from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from uuid import uuid4

class Contact(Base):
    __tablename__ = "Employees"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    phone_number = Column(String, index=True, unique=True)
    time = Column(DateTime, default=datetime.utcnow)
    salary = relationship("Salary", back_populates="owner")

class Salary(Base):
    __tablename__ = "Salary"
    id = Column(Integer, primary_key=True, nullable=False)     
    owner_id = Column(Integer, ForeignKey("Employees.id"))
    gross_pay= Column(Integer, index=True)
    bonus_payment = Column(Integer, index=True)
    payroll_deductions = Column(Integer, index=True)
    Reason = Column(String, index=True)
    if bonus_payment is None:
        net_pay_without_bonus = gross_pay - payroll_deductions
        net_pay = Column("%s", index=True ) %(net_pay_without_bonus)
    else:
        net_pay_with_bonus = (gross_pay + bonus_payment) - payroll_deductions 
        net_pay = Column("%s", index=True ) %(net_pay_with_bonus)
    time = Column(DateTime, default=datetime.utcnow)
    owner = relationship("Contact", back_populates="salary")

