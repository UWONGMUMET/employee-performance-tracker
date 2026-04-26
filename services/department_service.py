from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.department import Department

def create_department(db: Session, name: str, description: str):
    existing = db.query(Department).filter(Department.name == name).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Department already exists"
        )
    
    department = Department(
        name=name,
        description=description
    )

    db.add(department)
    db.commit()
    db.refresh(department)

    return department

def get_departments(db: Session):
    return db.query(Department).all()

def get_department_by_id(db: Session, department_id: str):
    department = db.query(Department).filter(Department.id == department_id).first()
    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )
    return department

def update_department(db: Session, department_id: str, data):
    department = db.query(Department).filter(Department.id == department_id).first()
    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )
    if data.name:
        department.name = data.name
    if data.description:
        department.description = data.description
    
    db.commit()
    db.refresh(department)
    return department

def delete_department(db: Session, department_id: str):
    department = db.query(Department).filter(Department.id == department_id).first()
    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )
    
    db.delete(department)
    db.commit()
    return {"message": "Department deleted successfully"}