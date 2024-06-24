from ..models import User
from ..db import SessionLocal

class AuthService:
    @staticmethod
    def login(user):
        db = SessionLocal()
        db_user = db.query(User).filter(User.username == user.username).first()
        if db_user and db_user.hashed_password == user.password:
            return {"username": db_user.username}
        return {"error": "Invalid credentials"}
