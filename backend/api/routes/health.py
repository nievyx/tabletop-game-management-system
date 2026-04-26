from fastapi import APIRouter
from backend.database.db import query_one

router = APIRouter(tags=['Health'])

@router.get("/")
def root():
    return {"message": "API is running"}

@router.get('/db-check') #http://127.0.0.1:8000/db-check
def db_check():
    row = query_one('SELECT 1 AS ok',())
    return row #should return {'ok' :1}

@router.get('/db-check-users-table') #http://127.0.0.1:8000/db-check-users-table
def db_check_users_table():
    row = query_one(
        'SELECT name FROM sqlite_master WHERE type="table" AND name="users"'
    )
    return {'users_table_exists': row is not None}