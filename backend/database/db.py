import sqlite3
import logging
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / 'app.db'

logger = logging.getLogger(__name__)

def get_db():
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()

def fetch_all(): #(..)
    pass

def fetch_one(): #(..)
    pass

def query_one(sql: str, params: tuple = ()):
    """Run a SELECT that returns 0 or 1 row"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys = ON;')

    try:
        logger.debug('Executing query_one..')
        row = conn.execute(sql, params).fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def query_all(sql: str, params: tuple = ()):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def execute(): #(...)
    pass

def get_connection(): # no arguments needed
    return sqlite3.connect(DB_PATH)

if __name__ == '__main__':
    if not DB_PATH.exists():
        print('FROM: db.py: Database does not exist')

    # result = query_one("SELECT name FROM sqlite_master WHERE type='table'")
