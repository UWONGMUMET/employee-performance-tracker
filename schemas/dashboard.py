from pydantic import BaseModel

class TopPerformer(BaseModel):
    employee_id: str
    employee_name: str
    average_score: float

class DashboardSummaryResponse(BaseModel):
    total_employees: int
    total_reviews: int
    average_company_score: float
    top_performers: TopPerformer | None