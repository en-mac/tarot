from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import cards

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cards.router, prefix="/api")
