import sys
from app.models import Base, engine

def create_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    if "create_db" in sys.argv:
        create_db()
