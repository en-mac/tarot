from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.card import CardResponse, FortuneHistoryResponse
from ..services.card_service import CardService
from ..db import get_db
from ..models import FortuneHistory

router = APIRouter()

@router.get("/draw_card", response_model=CardResponse)
def draw_card(db: Session = Depends(get_db)):
    card = CardService.draw_card()
    # Save to history
    fortune_history = FortuneHistory(card_name=card['card_name'], fortune_text=card['fortune_text'])
    db.add(fortune_history)
    db.commit()
    db.refresh(fortune_history)
    return card

@router.get("/fortune_history", response_model=FortuneHistoryResponse)
def get_fortune_history(db: Session = Depends(get_db)):
    history = db.query(FortuneHistory).all()
    return {"history": history}
