from fastapi import APIRouter, Depends, HTTPException
import sqlite3
from backend.database.db import get_db

router = APIRouter(prefix='/users',tags=['Users'])

@router.get('/')
def get_users(db: sqlite3.Connection = Depends(get_db)):
    rows = db.execute('SELECT * FROM users').fetchall()
    return [dict(row) for row in rows]

@router.post('/')
def create_users(username: str, email: str, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.execute(
        'INSERT INTO users (username, email) VALUES (?, ?)',
    (username, email)
    )
    db.commit()
    return {'user_id': cursor.lastrowid}

@router.get('/{user_id}')
def update_user(user_id: int, username: str, email: str, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.execute(
        'UPDATE users SET username = ?, email = ? WHERE user_id = ?',
        (username, email, user_id)
    )
    db.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail='User not found')

    return {'message': 'updated successfully'}

@router.delete('/{user_id}')
def delete_user(user_id: int, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.execute(
        'DELETE FROM users WHERE user_id = ?',
        (user_id,)
    )
    db.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail='User not found')

    return {'message': 'deleted successfully'}