from fastapi import FastAPI
from core.config import settings

app = FastAPI(
    title="Employee Performance Tracker API",
    debug=settings.DEBUG
)

@app.get("/")
def root():
    return {
        "message": "Employee Performance Tracker API Running"
    }