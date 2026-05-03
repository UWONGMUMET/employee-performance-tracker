from pydantic import BaseModel

class TopPerformer(BaseModel):
    employee_id: str
    employee_name: str
    average_score: float

class DashboardSummaryResponse(BaseModel):
    total_employees: int
    total_reviews: int
    average_score: float
    top_performer: TopPerformer | None

class DepartmentPerformance(BaseModel):
    department_id: str
    department_name: str
    average_score: float
    total_reviews: int