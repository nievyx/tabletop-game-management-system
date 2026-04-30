import sqlite3
import hashlib
from fastapi import APIRouter, Depends, HTTPException

from backend.database.db import get_db
from backend.app.models import PlayerCreate, PlayerUpdate

router = APIRouter(prefix='/players',tags=['Players'])

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# ==============================
#  PLAYERS CRUD
# ==============================

# ===== CREATE =====

@router.post('/')
def create_player(player: PlayerCreate, db : sqlite3.Connection = Depends(get_db)):
    hashed_password = hash_password(player.password_hash) # NOTE: Placeholder

    cursor = db.execute(
        '''
        INSERT INTO players (email, display_name, password_hash) 
        VALUES (?, ?, ?)
        ''',
    (player.email, player.display_name, hashed_password)
    )

    db.commit()

    return {'player_id': cursor.lastrowid}

# ===== READ =====

@router.get('/')
def get_player(db: sqlite3.Connection = Depends(get_db)):
    rows = db.execute('''
        SELECT 
            player_id,
            email,
            display_name,
            date_created
        FROM players
    ''').fetchall()

    return [dict(row) for row in rows]


# ===== UPDATE =====

@router.put('/{player_id}')
def update_player(
        player_id: int,
        player: PlayerUpdate,
        db: sqlite3.Connection = Depends(get_db)
):
    cursor = db.execute(
        """
        UPDATE players
        SET
            display_name = COALESCE(?, display_name),
            email = COALESCE(?, email),
            password_hash = COALESCE(?, password_hash)
        WHERE player_id = ?
        """,
        (
            player.display_name,
            player.email,
            hash_password(player.password_hash) if player.password_hash else None,
            player_id,
        ),
    )

    db.commit()


    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail='Player not found')

    return {'message': 'updated successfully'}

# ===== DELETE =====

@router.delete('/{player_id}')
def delete_player(player_id: int, db: sqlite3.Connection = Depends(get_db)):
    try:
        cursor = db.execute(
            '''
            DELETE FROM 
            players WHERE player_id = ?
            ''',
            (player_id,)
        )

        db.commit()

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail='Cannot delete this player because they are linked to other records'
        )

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail='Player not found')

    return {'message': 'deleted successfully'}