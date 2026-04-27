from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PerformanceReviewCreate(BaseModel):
    employee_id: str
    department_id: str
    score: int
    feedback: Optional[str] = None
    review_period: str

class PerformanceReviewUpdate(BaseModel):
    score: Optional[int] = None
    feedback: Optional[str] = None
    status: Optional[str] = None

class PerformanceReviewResponse(BaseModel):
    id: str
    employee_id: str
    reviewer_id: str
    department_id: str
    score: int 
    feedback: Optional[str]
    review_period: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True