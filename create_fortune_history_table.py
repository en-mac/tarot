import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

load_dotenv()

def create_fortune_history_table():
    db_url = os.getenv("DB_URL")
    if not db_url:
        raise ValueError("DB_URL environment variable is not set")

    conn = psycopg2.connect(db_url)
    cur = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS fortune_history (
        id SERIAL PRIMARY KEY,
        card_name VARCHAR(50) NOT NULL,
        fortune_text VARCHAR(255) NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    );
    """

    cur.execute(create_table_query)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_fortune_history_table()
