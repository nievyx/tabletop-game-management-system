import sqlite3
import logging
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / 'app.db'

logger = logging.getLogger(__name__)

def query_one(sql: str, params: tuple = ()): 
    '''Run a SELECT that returns 0 or 1 row'''
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys = ON;')

    try:
        logger.debug('Excuting query_one..')
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

    # result = query_one("SELECT name FROM sqlite_master WHERE type='table'")
