from db.session import SessionLocal
from models.user import User
from models.department import Department
from models.performance_review import PerformanceReview
from core.security import hash_password
import random

def seed():
    db = SessionLocal()

    # ======================
    # DEPARTMENTS
    # ======================
    existing_departments = db.query(Department).all()

    if existing_departments:
        print("Departments already seeded, skipping...")
        departments = existing_departments
    else:
        departments = [
            Department(name="Engineering", description="Backend & Frontend"),
            Department(name="HR", description="Human Resources"),
            Department(name="Marketing", description="Growth & Ads"),
            Department(name="Finance", description="Money & Budget")
        ]
        db.add_all(departments)
        db.commit()

        for dept in departments:
            db.refresh(dept)

        print("Departments seeded successfully")

    # ======================
    # USERS
    # ======================
    existing_users = db.query(User).count()

    if existing_users == 0:
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

        for user in users:
            db.refresh(user)

        print("Users seeded")
    else:
        users = db.query(User).all()
        print("Users already exist, skipping...")

    # ======================
    # REVIEWS
    # ======================
    existing_reviews = db.query(PerformanceReview).count()

    periods = ["Jan 2026", "Feb 2026", "Mar 2026", "Apr 2026"]

    if existing_reviews == 0:
        for _ in range(40):
            employee = random.choice(users)
            reviewer = random.choice(users)

            while reviewer.id == employee.id:
                reviewer = random.choice(users)

            review = PerformanceReview(
                employee_id=employee.id,
                reviewer_id=reviewer.id,
                department_id=random.choice(departments).id,
                score=random.randint(60, 100),
                feedback="Auto generated review",
                review_period=random.choice(periods),
                status="APPROVED"
            )
            db.add(review)

        db.commit()
        print("Reviews seeded")
    else:
        print("Reviews already exist, skipping...")

    db.close()
    print("Seed data created successfully!")

if __name__ == "__main__":
    seed()