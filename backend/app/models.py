from sqlalchemy import Column, Integer, String, DateTime, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .db import Base
from .config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class CardDraw(Base):
    __tablename__ = "card_draws"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    card_name = Column(String)
    fortune_text = Column(String)
    timestamp = Column(DateTime)


class FortuneHistory(Base):
    __tablename__ = "fortune_history"

    id = Column(Integer, primary_key=True, index=True)
    card_name = Column(String, index=True)
    fortune_text = Column(String)
    timestamp = Column(DateTime, server_default=func.now())
