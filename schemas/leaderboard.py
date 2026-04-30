from pydantic import BaseModel

class LeaderboarResponse(BaseModel):
    employee_id: str
    employee_name: str
    average_score: float
    total_reviews: int

class LeaderboardPaginatedResponse(BaseModel):
    data: list[LeaderboarResponse]
    page: int
    limit: int
    total: int