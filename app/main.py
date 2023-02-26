from fastapi import Depends, FastAPI, HTTPException
from typing import List
from sqlalchemy.orm import Session
import crud, schemas, models
from database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

'''-------------------------------- Employee Section --------------------------------'''
@app.post("/api/v1/contacts", response_model=schemas.Contact)
async def add_employee(contact: schemas.AddContact, db: Session = Depends(crud.get_db)): 
    return await crud.add_employee(contact=contact, db=db)

@app.get("/api/v1/contacts", response_model=List[schemas.Contact])
async def get_all_employees(
    db: Session = Depends(crud.get_db), 
    page: int = 1, 
    limit: int = 10,   
    #columns: str = None
    ): 
    return await crud.get_all_employees(db=db, page = page, limit = limit)#, columns=columns)

@app.get("/api/v1/contacts/{employee_id}", response_model=schemas.Contact)
async def get_employee_by_id(employee_id: int, db: Session = Depends(crud.get_db)): 
    employee = await crud.get_employee_by_id(employee_id=employee_id, db=db)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee does not exist")
    return employee

@app.delete("/api/v1/contacts/{employee_id}")
async def delete_contact(employee_id: int, db: Session = Depends(crud.get_db)):
    employee = await crud.get_employee_by_id(employee_id=employee_id, db=db)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee does not exist")
    else:
        await crud.delete_employee(employee, db=db)
        return "Employee deleted successfully"

@app.put("/api/v1/contacts/{employee_id}", response_model=schemas.Contact)
async def update_employee_info(employee_id: int, employee_data: schemas.AddContact, db: Session = Depends(crud.get_db)):
    employee = await crud.get_employee_by_id(employee_id=employee_id, db=db)
    if employee_id is None:
        raise HTTPException(status_code=404, detail="Employee does not exist")
    return await crud.update_contact(employee_data=employee_data, employee=employee, db=db)


'''-------------------------------- Salary Section --------------------------------'''

@app.post("/api/v1/salary/{employee_id}", response_model=schemas.Salary)
async def add_salary(employee_id: int, salary: schemas.AddSalary, db: Session = Depends(crud.get_db)): 
    employee = await crud.get_employee_by_id(employee_id=employee_id, db=db)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee does not exist")
    else:
        return await crud.add_salary(salary=salary, db=db, employee_id=employee_id)

@app.put("/api/v1/contacts/{employee_id}/salary", response_model=schemas.Salary)
async def update_contact(employee_id: int, salary_data: schemas.AddSalary, db: Session = Depends(crud.get_db)):
    employee = await crud.get_employee_by_id(employee_id=employee_id, db=db)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee does not exist")
    else:
        return await crud.update_salary(salary_data=salary_data, salary=employee, db=db)