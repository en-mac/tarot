from pydantic import BaseModel
from datetime import datetime

class FortuneHistoryResponse(BaseModel):
    history: list
