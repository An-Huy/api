from datetime import datetime
import schemas, models, database
from typing import List

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

    '''-------------------------------- Employee Section --------------------------------'''
async def add_employee(contact: schemas.AddContact, db: "database.Session") -> schemas.Contact: 
    contact = models.Contact(**contact.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return schemas.Contact.from_orm(contact)

async def get_all_employees(db: "database.Session") -> List[schemas.Contact]:
    contacts = db.query(models.Contact).all()
    return list(map(schemas.Contact.from_orm, contacts))

async def get_employee_by_id(employee_id: int, db: "database.Session") -> schemas.Contact:
    employee = db.query(models.Contact).filter(models.Contact.id == employee_id).first()
    return employee

async def delete_employee(employee: models.Contact, db: "database.Session") -> schemas.Contact:
    db.delete(employee)
    db.commit()

async def update_contact(employee_data: schemas.AddContact, employee: schemas.Contact, db: "database.Session") -> schemas.Contact:
    employee.first_name = employee_data.first_name
    employee.last_name = employee_data.last_name
    employee.email = employee_data.email
    employee.phone_number = employee_data.phone_number

    db.commit()
    db.refresh(employee)

    return schemas.Contact.from_orm(employee)

    '''-------------------------------- Salary Section --------------------------------'''
async def add_salary(salary: schemas.AddSalary, db: "database.Session") -> schemas.Salary: 
    salary = models.Salary(**salary.dict())
    db.add(salary)
    db.commit()
    db.refresh(salary)
    return schemas.Contact.from_orm(salary)

'''
async def get_salary_by_employee_id(employee_id: int, db: "database.Session") -> schemas.Salary:
    salary = db.query(models.Salary).filter(models.Salary.owner == employee_id).first()
    return salary

async def update_salary(salary_data: schemas.AddContact, salary: schemas.Contact, db: "database.Session") -> schemas.Salary:
    salary.gross_pay = salary_data.gross_pay
    salary.payroll_deductions = salary_data.payroll_deductions
    salary.Reason = salary_data.Reason

    db.commit()
    db.refresh(salary)

    return schemas.Salary.from_orm(salary)
'''