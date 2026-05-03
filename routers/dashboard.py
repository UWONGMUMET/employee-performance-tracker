from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.dashboard import DashboardSummaryResponse, DepartmentPerformance
from services.dashboard_service import get_dashboard_stats, get_dashboard_summary, get_department_performance
from core.dependencies import admin_required

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/", dependencies=[Depends(admin_required)])
def dashboard(db: Session = Depends(get_db)):
    return get_dashboard_stats(db)

@router.get("/summary", response_model=DashboardSummaryResponse, dependencies=[Depends(admin_required)])
def dashboard_summary(db: Session = Depends(get_db)):
    return get_dashboard_summary(db)

@router.get("/department-performance", response_model=DepartmentPerformance, dependencies=[Depends(admin_required)])
def department_performance(db: Session = Depends(get_db)):
    return get_department_performance(db)