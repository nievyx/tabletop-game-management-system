from datetime import datetime
from fastapi import APIRouter, HTTPException
from backend.database.db import get_db

router = APIRouter(prefix="/character_quests", tags=["character_quests"])

@router.patch('/{character_quest_id}/complete')
def complete_quest(character_quest_id: int):
    db = get_db()

    cursor = db.execute(
        '''
        UPDATE character_quests
        SET completed_at = CURRENT_TIMESTAMP
        WHERE character_quest_id = %s
        ''',
        (datetime.now().isoformat(timespec='seconds'),character_quest_id)

    )
    db.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Quest not found")

    return {
        'message': 'Quest completed successfully',
        'character_quest_id': character_quest_id
    }

#TODO: Connect to frontend
'''
fetch(`${API_BASE}/character-quests/${id}/complete`, {
  method: "PATCH"
})
'''
