from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from services.dashboard_service import get_dashboard_stats
from core.dependencies import admin_required

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/", dependencies=[Depends(admin_required)])
def dashboard(db: Session = Depends(get_db)):
    return get_dashboard_stats(db)