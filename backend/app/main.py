from fastapi import FastAPI
from .routes import auth, cards, history, about

app = FastAPI()

app.include_router(auth.router)
app.include_router(cards.router)
app.include_router(history.router)
app.include_router(about.router)
