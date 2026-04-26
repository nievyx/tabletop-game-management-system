from backend.database.db import get_db
from backend.api.repositories import get_all_users

from fastapi import APIRouter, Depends
from backend.database.db import query_one, query_all

router = APIRouter(tags=['Users'])

@router.get('/users')
def get_users():
    rows = query_all('SELECT user_id, username, email FROM users')
    return rows

