from fastapi import APIRouter
from backend.database.db import query_all

router = APIRouter(tags=['Profiles'])

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