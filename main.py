from fastapi import FastAPI
from core.config import settings

from routers import auth, user, dashboard, department, performance_review, leaderboard

app = FastAPI(
    title="Employee Performance Tracker API",
    debug=settings.DEBUG
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(dashboard.router)
app.include_router(department.router)
app.include_router(performance_review.router)
app.include_router(leaderboard.router)

@app.get("/")
def root():
    return {
        "message": "Employee Performance Tracker API Running"
    }