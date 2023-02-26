from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Contact(Base):
    __tablename__ = "Employees"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    sex = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    phone_number = Column(String, index=True, unique=True)
    time = Column(DateTime, default=datetime.utcnow)
    salary = relationship("Salary", back_populates="employee")

class Salary(Base):
    __tablename__ = "Salary"
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)  
    employee_id = Column(Integer, ForeignKey("Employees.id"))
    note = Column(String, index=True)
    salary = Column(Integer, index=True ) 
    time = Column(DateTime, default=datetime.utcnow)
    employee = relationship("Contact", back_populates="salary")