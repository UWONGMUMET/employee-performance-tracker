from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.leaderboard import LeaderboarResponse, LeaderboardPaginatedResponse
from services.leaderboard_service import get_leaderboard

router = APIRouter(prefix="/leaderboard", tags=["Leaderboard"])

@router.get("/", response_model=list[LeaderboardPaginatedResponse])
def get_leaderboard_endpoint(
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=100),
    review_period: str | None = None,
    db: Session = Depends(get_db)
):
    return get_leaderboard(db, page, limit, review_period)