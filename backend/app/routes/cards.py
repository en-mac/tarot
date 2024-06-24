from fastapi import APIRouter, Depends
from ..schemas.card import CardResponse
from ..services.card_service import CardService

router = APIRouter()

@router.get("/draw_card", response_model=CardResponse)
def draw_card():
    return CardService.draw_card()
