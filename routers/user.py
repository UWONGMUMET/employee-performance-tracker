from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.user import UserResponse, UserUpdate
from services.user_service import get_users, get_user_by_id, update_user, delete_user
from core.dependencies import get_current_user, admin_required

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/{user_id}", response_model=UserResponse, dependencies=[Depends(admin_required)])
def get_user(user_id: str, db: Session = Depends(get_db)):
    return get_user_by_id(db, user_id)

@router.put("/{user_id}", response_model=UserResponse, dependencies=[Depends(admin_required)])
def update_user_endpoint(user_id: str, data: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user_id, data)

@router.delete("/{user_id}", dependencies=[Depends(admin_required)])
def delete_user_endpoint(user_id: str, db: Session = Depends(get_db)):
    return delete_user(db, user_id, get_current_user())