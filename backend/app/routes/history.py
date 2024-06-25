from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from ..models import FortuneHistory

router = APIRouter()

@router.get("/fortune_history")
def get_fortune_history(db: Session = Depends(get_db)):
    history = db.query(FortuneHistory).all()
    return {"history": [h.to_dict() for h in history]}
