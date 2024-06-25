from pydantic import BaseModel
from datetime import datetime
from typing import List

class CardResponse(BaseModel):
    card_name: str
    fortune_text: str

class FortuneHistoryItem(BaseModel):
    card_name: str
    fortune_text: str
    timestamp: datetime

    class Config:
        orm_mode = True

class FortuneHistoryResponse(BaseModel):
    history: List[FortuneHistoryItem]
