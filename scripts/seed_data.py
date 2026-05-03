from db.session import SessionLocal
from models.user import User
from models.department import Department
from models.performance_review import PerformanceReview
from core.security import hash_password
import random


def seed():
    db = SessionLocal()

    departments = [
        Department(name="Engineering", description="Backend & Frontend"),
        Department(name="HR", description="Human Resources"),
        Department(name="Marketing", description="Growth & Ads"),
        Department(name="Finance", description="Money & Budget")
    ]

    db.add_all(departments)
    db.commit()

    users = []
    for i in range(15):
        user = User(
            name=f"Employee {i+1}",
            email=f"user{i+1}@example.com",
            password=hash_password("password123"),
            role="EMPLOYEE"
        )
        users.append(user)

    db.add_all(users)
    db.commit()

    periods = ["Jan 2026", "Feb 2026", "Mar 2026", "Apr 2026"]

    for _ in range(40):
        review = PerformanceReview(
            employee_id=random.choice(users).id,
            reviewer_id=random.choice(users).id,
            department_id=random.choice(departments).id,
            score=random.randint(60, 100),
            feedback="Auto generated review",
            review_period=random.choice(periods),
            status="APPROVED"
        )
        db.add(review)

    db.commit()
    db.close()

    print("🔥 Seed data created successfully!")

if __name__ == "__main__":
    seed()