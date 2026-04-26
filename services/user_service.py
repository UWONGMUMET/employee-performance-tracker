from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.user import User
from core.security import hash_password

def get_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user

def update_user(db: Session, user_id: str, data):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    if data.name:
        user.name = data.name
    if data.email:
        user.email = data.email
    if data.password:
        user.password = hash_password(data.password)
    if data.role:
        user.role = data.role
    if data.is_active is not None:
        user.is_active = data.is_active
    
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: str, current_user):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    if user.id == current_user.get("sub"):
        raise HTTPException(
            status_code=403,
            detail="Cannot delete yourself"
        )
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}