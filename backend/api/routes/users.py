import sqlite3
import hashlib
from fastapi import APIRouter, Depends, HTTPException
from backend.database.db import get_db
from backend.api.models import UserCreate, UserUpdate

router = APIRouter(prefix='/users',tags=['Users'])

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# ==============================
#  USERS CRUD
# ==============================

# ===== CREATE =====
# POST /users/

@router.post('/')
def create_user(user: UserCreate, db : sqlite3.Connection = Depends(get_db)):
    hashed_password = hash_password(user.password_hash) # NOTE: Placeholder

    cursor = db.execute(
        'INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
    (user.username, user.email, hashed_password)
    )
    db.commit()
    return {'user_id': cursor.lastrowid}

# ===== READ =====
# GET /users/

@router.get('/')
def get_users(db: sqlite3.Connection = Depends(get_db)):
    rows = db.execute('SELECT * FROM users').fetchall()
    return [dict(row) for row in rows]


# ===== UPDATE =====
# PUT /users/{user_id}

@router.put('/{user_id}')
def update_user(user_id: int, user: UserUpdate, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.execute(
        'UPDATE users SET username = ?, email = ? WHERE user_id = ?',
        (user.username, user.email, user_id)
    )
    db.commit()


    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail='User not found')

    return {'message': 'updated successfully'}

# ===== DELETE =====
# DELETE /users/{user_id}

@router.delete('/{user_id}')
def delete_user(user_id: int, db: sqlite3.Connection = Depends(get_db)):
    try:
        cursor = db.execute(
            'DELETE FROM users WHERE user_id = ?',
            (user_id,)
        )
        db.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail='Cannot delete this user because they are linked to other records'
        )

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail='User not found')

    return {'message': 'deleted successfully'}