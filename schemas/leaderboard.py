from pydantic import BaseModel

class LeaderboardResponse(BaseModel):
    employee_id: str
    employee_name: str
    average_score: float
    total_reviews: int

class LeaderboardPaginatedResponse(BaseModel):
    data: list[LeaderboardResponse]
    page: int
    limit: int
    total: int