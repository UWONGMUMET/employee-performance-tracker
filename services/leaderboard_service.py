from sqlalchemy.orm import Session
from sqlalchemy import func

from models.performance_review import PerformanceReview
from models.user import User

def get_leaderboard(db: Session):
    results = db.query(
        User.id.label("employee_id"),
        User.name.label("employee_name"),
        User.name.label("employee_name"),
        func.avg(PerformanceReview.score).label("average_score"),
        func.count(PerformanceReview.id).label("total_reviews")
    ).join(
        PerformanceReview, PerformanceReview.employee_id == User.id
    ).group_by(User.id).order_by(func.avg(PerformanceReview.score).desc()).all()

    return [
        {
            "employee_id": r.employee_id,
            "employee_name": r.employee_name,
            "average_score": r.average_score,
            "total_reviews": r.total_reviews
        }
        for r in results
    ]