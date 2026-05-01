from sqlalchemy.orm import Session
from sqlalchemy import func 

from models.user import User
from models.performance_review import PerformanceReview

def get_dashboard_stats(db: Session):
    total_users = db.query(
        func.count(User.id)
    ).scalar()

    active_users = db.query(
        func.count(User.id)
    ).filter(
        User.is_active == True
    ).scalar()

    inactive_users = db.query(
        func.count(User.id)
    ).filter(
        User.is_active == False
    ).scalar()

    admins = db.query(
        func.count(User.id)
    ).filter(
        User.role == "ADMIN"
    ).scalar()

    employees = db.query(
        func.count(User.id)
    ).filter(
        User.role == "EMPLOYEE"
    ).scalar()

    return {
        "total_users": total_users,
        "active_users": active_users,
        "inactive_users": inactive_users,
        "admins": admins,
        "employees": employees
    }

def get_dashboard_summary(db: Session):
    total_employees = db.query(User).count()
    total_reviews = db.query(PerformanceReview).count()

    avg_score = db.query(
        func.avg(PerformanceReview.score)
    ).scalar()
    avg_score = float(avg_score) if avg_score else 0.0

    top = db.query(
        User.id.label("employee_id"),
        User.name.label("employee_name"),
        func.avg(PerformanceReview.score).label("average_score")
    ).join(
        PerformanceReview, PerformanceReview.employee_id == User.id
    ).group_by(User.id).order_by(func.avg(PerformanceReview.score).desc()).first()

    top_performer = None
    if top:
        top_performer = {
            "employee_id": top.employee_id,
            "employee_name": top.employee_name,
            "average_score": float(top.average_score)
        }

    return {
        "total_employees": total_employees,
        "total_reviews": total_reviews,
        "average_score": avg_score,
        "top_performer": top_performer
    }