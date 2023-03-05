from fastapi import Depends, FastAPI, HTTPException
from typing import List
from sqlalchemy.orm import Session
import crud, schemas, models
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

'''-------------------------------- Employee Section --------------------------------'''
@app.post("/api/v1/contacts", response_model=schemas.Contact)
async def add_contact(contact: schemas.AddContact, db: Session = Depends(crud.get_db)): 
    return await crud.add_contact(contact=contact, db=db)

@app.get("/api/v1/contacts", response_model=List[schemas.Contact])
async def get_all_contacts(
    db: Session = Depends(crud.get_db), 
    page: int = 1, 
    limit: int = 10,   
    ): 
    return await crud.get_all_contacts(db=db, page = page, limit = limit)

@app.get("/api/v1/contacts/{owner_id}", response_model=schemas.Contact)
async def get_contact_by_id(contact_id: int, db: Session = Depends(crud.get_db)): 
    contact = await crud.get_contact_by_id(contact_id=contact_id, db=db)
    if contact is None:
        raise HTTPException(status_code=404, detail="Employee does not exist")
    return contact

@app.delete("/api/v1/contacts/{owner_id}")
async def delete_contact(contact_id: int, db: Session = Depends(crud.get_db)):
    contact = await crud.get_employee_by_id(contact_id=contact_id, db=db)
    if contact is None:
        raise HTTPException(status_code=404, detail="Employee does not exist")
    else:
        await crud.delete_contact(contact, db=db)
        return "Employee deleted successfully"

@app.put("/api/v1/contacts/{owner_id}", response_model=schemas.Contact)
async def update_contact_info(contact_data: schemas.AddContact, contact_id: int, db: Session = Depends(crud.get_db)):
    contact = await crud.get_employee_by_id(contact_id=contact_id, db=db)
    if contact is None:
        raise HTTPException(status_code=404, detail="Employee does not exist")
    return await crud.update_contact(contact_data=contact_data, contact=contact, db=db)


'''-------------------------------- Salary Section --------------------------------'''

@app.post("/api/v1/salary/{owner_id}", response_model=schemas.Salary)
async def add_salary(contact_id: int, salary: schemas.AddSalary, db: Session = Depends(crud.get_db)): 
    contact = await crud.get_employee_by_id(contact_id=contact_id, db=db)
    if contact is None:
        raise HTTPException(status_code=404, detail="Employee does not exist")
    else:
        return await crud.add_salary(contact_id=contact_id, salary=salary, db=db)

@app.put("/api/v1/contacts/{employee_id}/salary", response_model=schemas.Salary)
async def update_contact(employee_id: int, salary_data: schemas.AddSalary, db: Session = Depends(crud.get_db)):
    employee = await crud.get_employee_by_id(employee_id=employee_id, db=db)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee does not exist")
    else:
        return await crud.update_salary(salary_data=salary_data, salary=employee, db=db)