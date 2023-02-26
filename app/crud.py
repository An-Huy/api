import schemas, models, database
from sqlalchemy import column
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

def convert_columns(columns):
    return list(map(lambda x: column(x), columns.split('-')))

async def get_all_employees(db: "database.Session", page: int = 1, limit: int = 10) -> List[schemas.Contact]:
                            #, columns: str = None) -> List[schemas.Contact]:
    '''  
    if columns is not None and columns != "all":
        contacts = db.query(models.Contact, columns=convert_columns(columns))
    '''
    contacts = db.query(models.Contact).offset(page).limit(limit).all()
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

async def add_salary(salary: schemas.AddSalary, db: "database.Session", employee_id: int) -> schemas.Salary: 
    salary = models.Salary(**salary.dict(), employee_id = employee_id)
    db.add(salary)
    db.commit()
    db.refresh(salary)
    return schemas.Salary.from_orm(salary)

async def update_salary(salary_data: schemas.AddSalary, salary: schemas.Salary, db: "database.Session") -> schemas.Salary:
    salary.note = salary_data.note
    salary.salary = salary_data.salary

    db.commit()
    db.refresh(salary)

    return schemas.Salary.from_orm(salary)