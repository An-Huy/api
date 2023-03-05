import schemas, models, database
from typing import List

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

    '''-------------------------------- Employee Section --------------------------------'''
async def add_contact(contact: schemas.AddContact, db: "database.Session") -> schemas.Contact: 
    contact = models.Contact(**contact.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return schemas.Contact.from_orm(contact)

async def get_all_contacts(db: "database.Session", page: int = 1, limit: int = 10) -> List[schemas.Contact]:
    contacts = db.query(models.Contact).offset(page).limit(limit).all()
    return list(map(schemas.Contact.from_orm, contacts))

async def get_contact_by_id(owner_id: int, db: "database.Session") -> schemas.Contact:
    employee = db.query(models.Contact).filter(models.Contact.id == owner_id).first()
    return employee

async def delete_contact(contact: models.Contact, db: "database.Session") -> schemas.Contact:
    db.delete(contact)
    db.commit()

async def update_contact(contact_data: schemas.AddContact, contact: schemas.Contact, db: "database.Session") -> schemas.Contact:
    contact.first_name = contact_data.first_name
    contact.last_name = contact_data.last_name
    contact.email = contact_data.email
    contact.phone_number = contact_data.phone_number

    db.commit()
    db.refresh(contact)

    return schemas.Contact.from_orm(contact)

    '''-------------------------------- Salary Section --------------------------------'''

async def add_salary(salary: schemas.AddSalary, db: "database.Session", owner_id: int) -> schemas.Salary: 
    salary = models.Salary(**salary.dict(), owner_id = owner_id)
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