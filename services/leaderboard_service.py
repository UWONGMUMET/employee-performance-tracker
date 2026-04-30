from sqlalchemy.orm import Session
from sqlalchemy import func

from models.performance_review import PerformanceReview
from models.user import User

def get_leaderboard(db: Session, page: int = 1, limit: int = 10, review_period: str | None = None):
    query = db.query(
        User.id.label("employee_id"),
        User.name.label("employee_name"),
        func.avg(PerformanceReview.score).label("average_score"),
        func.count(PerformanceReview.id).label("total_reviews")
    ).join(
        PerformanceReview, PerformanceReview.employee_id == User.id
    )

    if review_period:
        query = query.filter(PerformanceReview.review_period == review_period)

    query = query.group_by(User.id)
    total = query.count()

    results = query.order_by(func.avg(PerformanceReview.score).desc()).offset((page - 1) * limit).limit(limit).all()

    return {
        "data": [
            {
                "employee_id": r.employee_id,
                "employee_name": r.employee_name,
                "average_score": r.average_score,
                "total_reviews": r.total_reviews
            }
            for r in results
        ],
        "page": page,
        "limit": limit,
        "total": total
    }