from pydantic import BaseModel

class CardResponse(BaseModel):
    card_name: str
    fortune_text: str
