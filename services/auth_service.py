from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.user import User
from core.security import hash_password, verify_password, create_access_token

def register_user(db: Session, name: str, email: str, password: str):
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    user = User(
        name=name,
        email=email,
        password=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Invalid credentials"
        )
    
    if not verify_password(password, user.password):
        raise HTTPException(
            status_code=400,
            detail="Invalid credentials"
        )
    
    access_token = create_access_token({
        "sub": user.id,
        "role": user.role,
        "email": user.email
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

