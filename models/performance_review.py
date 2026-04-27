from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
import uuid

from db.base import Base

class PerformanceReview(Base):
    __tablename__ = "performance_reviews"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    employee_id = Column(String, ForeignKey("users.id"), nullable=False)
    reviewer_id = Column(String, ForeignKey("users.id"), nullable=False)
    department_id = Column(String, ForeignKey("departments.id"), nullable=False)
    score = Column(Integer, nullable=False)
    feedback = Column(String, nullable=True)
    review_period = Column(String, nullable=False)
    status = Column(String, default="PENDING")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)