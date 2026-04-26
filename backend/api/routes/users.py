from fastapi import APIRouter, Depends
import sqlite3
from backend.database.db import get_db

router = APIRouter(prefix='/users',tags=['Users'])

@router.get('/')
def get_users(db: sqlite3.Connection = Depends(get_db)):
    rows = db.execute('SELECT * FROM users').fetchall()
    return [dict(row) for row in rows]

