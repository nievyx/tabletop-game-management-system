import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / 'app.db'

def query_one(sql, params): #(...)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.excute('PRAGMA foreign_keys = ON;')

    try:
        row = conn.execute(sql, params).fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def query_all(): #(...)
    pass

def execute(): #(...)
    pass

def get_conn(): # no arguements needed
    pass


if __name__ == '__main__':
    if not DB_PATH.exists():
        print('Database does not exist')