from fastapi import APIRouter, HTTPException
from backend.database.db import get_db
from backend.app.models.character import CharacterCreate
from backend.database.db import query_all

router = APIRouter(prefix='/characters',tags=['Characters'])

@router.get('/')
def get_characters():
    rows = query_all("""
        SELECT 
            c.character_id AS id,
            c.character_name,
            c.level,
            c.character_type,
            cl.class_name,
            s.species_name,
            a.alignment_name,
            p.display_name AS player_name
        FROM characters c
        JOIN players p ON c.player_id = p.player_id
        JOIN classes cl ON c.class_id = cl.class_id
        JOIN species s ON c.species_id = s.species_id
        JOIN alignments a ON c.alignment_id = a.alignment_id
        ORDER BY c.character_id;
    """)
    return rows

@router.get('/{character_id}')
def get_character(character_id: int):
    rows = query_all("""
        SELECT
         c.character_id AS id,
            c.character_name,
            c.level,
            c.character_type,
            cl.class_name,
            s.species_name,
            a.alignment_name,
            p.display_name AS player_name
        FROM characters c
        JOIN players p ON c.player_id = p.player_id
        JOIN classes cl ON c.class_id = cl.class_id
        JOIN species s ON c.species_id = s.species_id
        JOIN alignments a ON c.alignment_id = a.alignment_id
        WHERE c.character_id = ?
    """, (character_id,))

    if not rows:
        raise HTTPException(status_code=404, detail="Character not found")

    return rows[0]

@router.post('/')
def create_character(character: CharacterCreate):
    try:
        query = '''
        INSERT INTO characters (
            player_id,
            character_name,
            character_type,
            class_id,
            species_id,
            alignment_id,
            level
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        '''

        params = (
            character.player_id,
            character.character_name,
            character.character_type,
            character.class_id,
            character.species_id,
            character.alignment_id,
            character.level
        )

        db = get_db()
        cursor = db.execute(query, params)
        db.commit()

        return {
            'message': 'Character created successfully',
            'character_id': cursor.lastrowid
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


