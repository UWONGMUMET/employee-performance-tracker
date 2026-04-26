from sqlalchemy.orm import Session
from sqlalchemy import func 

from models.user import User

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