from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from core.security import get_current_user, admin_required

from schemas.performance_review import PerformanceReviewResponse, PerformanceReviewCreate, PerformanceReviewUpdate
from services.performance_review_service import create_review, get_reviews, update_review, delete_review

router = APIRouter(prefix="/performance-reviews", tags=["Performance Reviews"])

@router.post("/", response_model=PerformanceReviewResponse, dependencies=[Depends(admin_required)])
def create_review_endpoint(data: PerformanceReviewCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_review(db, user, data)

@router.get("/", response_model=list[PerformanceReviewResponse])
def get_all_reviews(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return get_reviews(db, user)

@router.put("/{review_id}", response_model=PerformanceReviewResponse, dependencies=[Depends(admin_required)])
def update_review_endpoint(review_id: str, data: PerformanceReviewUpdate, db: Session = Depends(get_db)):
    return update_review(db, review_id, data)

@router.delete("/{review_id}", dependencies=[Depends(admin_required)])
def delete_review_endpoint(review_id: str, db: Session = Depends(get_db)):
    return delete_review(db, review_id)