from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.department import DepartmentResponse, DepartmentCreate, DepartmentUpdate
from services.department_service import create_department, get_departments, get_department_by_id, update_department, delete_department
from core.dependencies import admin_required

router = APIRouter(prefix="/departments", tags=["Departments"])

@router.post("/", response_model=DepartmentResponse, dependencies=[Depends(admin_required)])
def create_department_endpoint(data: DepartmentCreate, db: Session = Depends(get_db)):
    return create_department(db, data.name, data.description)

@router.get("/", response_model=list[DepartmentResponse])
def get_all_departments(db: Session = Depends(get_db)):
    return get_departments(db)

@router.get("/{department_id}", response_model=DepartmentResponse)
def get_department(department_id: str, db: Session = Depends(get_db)):
    return get_department_by_id(db, department_id)

@router.put("/{department_id}", response_model=DepartmentResponse, dependencies=[Depends(admin_required)])
def update_department(department_id: str, data: DepartmentUpdate, db: Session = Depends(get_db)):
    return update_department(db, department_id, data)

@router.delete("/{department_id}", dependencies=[Depends(admin_required)])
def delete_department(department_id: str, db: Session = Depends(get_db)):
    return delete_department(db, department_id)