from fastapi import APIRouter
from backend.database.db import query_all

router = APIRouter(tags=['Characters'])

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
