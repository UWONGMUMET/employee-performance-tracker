from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.leaderboard import LeaderboarResponse
from services.leaderboard_service import get_leaderboard

router = APIRouter(prefix="/leaderboard", tags=["Leaderboard"])

@router.get("/", response_model=list[LeaderboarResponse])
def get_leaderboard_endpoint(db: Session = Depends(get_db)):
    return get_leaderboard(db)