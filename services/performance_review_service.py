from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.performance_review import PerformanceReview

def create_review(db: Session, user, data):
    review = PerformanceReview(
        employee_id=data.employee_id,
        reviewer_id=user.get("sub"),
        department_id=data.department_id,
        score=data.score,
        feedback=data.feedback,
        review_period=data.review_period
    )

    db.add(review)
    db.commit()
    db.refresh(review)

    return review

def get_reviews(db: Session, user):
    if user.get("role") == "ADMIN":
        return db.query(PerformanceReview).all()
    return db.query(PerformanceReview).filter(PerformanceReview.employee_id == user.get("sub")).all()

def update_review(db: Session, review_id: str, data):
    review = db.query(PerformanceReview).filter(PerformanceReview.id == review_id).first()
    if not review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )
    if data.score is not None:
        review.score = data.score
    if data.feedback is not None:
        review.feedback = data.feedback
    if data.status is not None:
        review.status = data.status
    
    db.commit()
    db.refresh(review)
    return review

def delete_review(db: Session, review_id: str):
    review = db.query(PerformanceReview).filter(PerformanceReview.id == review_id).first()
    if not review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )
    
    db.delete(review)
    db.commit()
    return {"message": "Review deleted successfully"}