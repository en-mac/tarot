from ..models import CardDraw
from ..db import SessionLocal

class FortuneService:
    @staticmethod
    def get_history():
        db = SessionLocal()
        history = db.query(CardDraw).all()
        return {"history": history}
