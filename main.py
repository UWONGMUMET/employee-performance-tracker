from fastapi import FastAPI
from core.config import settings

from routers import auth, user

app = FastAPI(
    title="Employee Performance Tracker API",
    debug=settings.DEBUG
)

app.include_router(auth.router)
app.include_router(user.router)

@app.get("/")
def root():
    return {
        "message": "Employee Performance Tracker API Running"
    }