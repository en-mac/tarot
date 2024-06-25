import os
import psycopg2
from psycopg2 import sql
from app.models import Base, engine
from dotenv import load_dotenv
from urllib.parse import urlparse, urlunparse

load_dotenv()

def create_database():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise ValueError("DATABASE_URL environment variable is not set")

    parsed_url = urlparse(db_url)
    db_name = parsed_url.path[1:]

    conn_params = urlunparse(parsed_url._replace(path='/postgres'))

    conn = psycopg2.connect(conn_params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [db_name])
    exists = cur.fetchone()
    if not exists:
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
        print(f"Database {db_name} created.")
    else:
        print(f"Database {db_name} already exists.")

    cur.close()
    conn.close()

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created.")

if __name__ == "__main__":
    create_database()
    create_tables()
