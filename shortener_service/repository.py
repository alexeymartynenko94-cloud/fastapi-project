import sqlite3
from pathlib import Path

DB_FILE = Path("data/links.db")


def connect():
    DB_FILE.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_FILE)


def init_storage():
    with connect() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS links (
                code TEXT PRIMARY KEY,
                original TEXT NOT NULL
            )
            """
        )


def save_link(code: str, url: str):
    with connect() as conn:
        conn.execute(
            "INSERT INTO links (code, original) VALUES (?, ?)",
            (code, url)
        )
        conn.commit()


def fetch_link(code: str):
    with connect() as conn:
        cur = conn.cursor()
        cur.execute("SELECT original FROM links WHERE code = ?", (code,))
        row = cur.fetchone()
        return row[0] if row else None
