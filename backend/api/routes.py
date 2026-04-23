from fastapi import APIRouter
from backend.database.db import query_one, query_all

router = APIRouter()

@router.get("/")
def root():
    return {"message": "API is running"}

@router.get('/users')
def get_users():
    rows = query_all('SELECT user_id, username, email FROM users')
    return rows

@router.get('/db-check') #http://127.0.0.1:8000/db-check
def deb_check():
    row = query_one('SELECT 1 AS ok',())
    return row #should return {'ok' :1}

@router.get('/db-check-users-table') #http://127.0.0.1:8000/db-check-users-table
def db_check_users_table():
    row = query_one(
        'SELECT name FROM sqlite_master WHERE type="table" AND name="users"'
    )
    return {'users_table_exists': row is not None}

@router.get('/profiles')
def get_profiles():
    rows = query_all("""
        SELECT 
            profile_id AS id, 
            user_id, 
            display_name, 
            created_at
        FROM profiles
    """)
    return rows

@router.get('/characters')
def get_characters():
    rows = query_all("""
        SELECT 
            p.profile_id AS id,
            p.display_name,
            c.level,
            cl.name AS class_name
        FROM profiles p
        JOIN characters c ON p.profile_id = c.profile_id
        JOIN classes cl ON c.class_id = cl.class_id
    """)
    return rows

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