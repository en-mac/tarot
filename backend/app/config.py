import os

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/tarotapp")
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

settings = Settings()
