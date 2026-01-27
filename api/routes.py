from fastapi import APIRouter
from database.db import query_one

router = APIRouter()

@router.get('/db-check')
def deb_check():
    row = query_one('SELECT 1 AS ok',())
    return row #should  return {'ok' :1}

@router.get('/db-check-users-table') #http://127.0.0.1:8000/db-check-users-table
def db_check_users_table():
    row = query_one(
        'SELECT name FROM sqlite_master WHERE type="table" AND name="users"'
    )
    return {'users_table_exists': row is not None}

'''
HOW TO RUN (Windows / Powershell):

Start the development server from the project root:
uvicorn api.main:app --reload

Go to in browser:
http://127.0.0.1:8000/db-check

Success result:
INFO:     127.0.0.1:64463 - "GET /db-check HTTP/1.1" 200 OK

( HTTP 200 OK
Response body: {"ok": 1} )

'''