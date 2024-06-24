from fastapi import APIRouter, Depends
from ..schemas.fortune import FortuneHistoryResponse
from ..services.fortune_service import FortuneService

router = APIRouter()

@router.get("/fortune_history", response_model=FortuneHistoryResponse)
def get_fortune_history():
    return FortuneService.get_history()
