import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / 'app.db'

def query_one(): #(...)
    pass

def query_all(): #(...)
    pass

def execute(): #(...)
    pass

def get_conn(): # no arguements needed
    pass


if __name__ == '__main__':
    if not DB_PATH.exists():
        print('Database does not exist')