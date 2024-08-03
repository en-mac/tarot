from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.card import CardResponse, FortuneHistoryResponse
from ..services.card_service import CardService
from ..db import get_db
from ..models import FortuneHistory

router = APIRouter()

@router.get("/fortune_history", response_model=FortuneHistoryResponse)
def get_fortune_history(db: Session = Depends(get_db)):
    history = db.query(FortuneHistory).all()
    return {"history": history}
