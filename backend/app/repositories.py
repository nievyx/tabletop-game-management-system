from fastapi import HTTPException

from backend.database import db
from backend.database.db import get_db

def _fetchone_or_404(db, query, params=(), detail='Not Found'):
    row = db.execute(query, params).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail=detail)
    return dict(row)

def get_all_users(db) -> list[dict]:
    rows = db.execute('SELECT user_id, email FROM users').fetchall()
    return [dict(row) for row in rows]

class CharacterRepository:

    BASE_QUERY = """
        SELECT
            ch.character_id,
            ch.profile_id,
            p.display_name,
            ch.class_id,
            c.name AS class_name,
            ch.level
        FROM characters ch
        JOIN profiles p ON ch.profile_id = p.profile_id
        JOIN classes c ON ch.class_id = c.class_id
    """

    def get_all(self):
        with get_db() as conn:
            return conn.execute(
                self.BASE_QUERY + " ORDER BY p.display_name"
            ).fetchall()

    def get_by_id(self, character_id: int):
        with get_db() as conn:
            return _fetchone_or_404(
                conn,
                self.BASE_QUERY + " WHERE ch.character_id = ?",
                (character_id,)
            )

    def create(self, data: dict) -> int:
        with get_db() as conn:
            cursor = conn.execute("""
                                  INSERT INTO characters (profile_id, class_id, level)
                                  VALUES (?, ?, ?)
                                  """, (
                                      data["profile_id"],
                                      data["class_id"],
                                      data["level"],
                                  ))
            conn.commit()
            return cursor.lastrowid

    def update(self, character_id: int, data: dict) -> None:
        with get_db() as conn:
            conn.execute("""
                         UPDATE characters
                         SET profile_id = ?,
                             class_id   = ?,
                             level      = ?
                         WHERE character_id = ?
                         """, (
                             data["profile_id"],
                             data["class_id"],
                             data["level"],
                             character_id,
                         ))
            conn.commit()

    def delete(self, character_id: int) -> None:
        with get_db() as conn:
            conn.execute(
                "DELETE FROM characters WHERE character_id = ?",
                (character_id,)
            )
            conn.commit()

class AssetRepository:

    BASE_QUERY = """
        SELECT
            a.asset_id,
            a.title,
            a.asset_type_id,
            at.name AS asset_type_name
        FROM assets a
        JOIN asset_types at ON a.asset_type_id = at.asset_type_id
    """

    def get_all(self):
        with get_db() as conn:
            return conn.execute(
                self.BASE_QUERY + " ORDER BY a.title"
            ).fetchall()

    def get_by_id(self, asset_id: int):
        with get_db() as conn:
            return _fetchone_or_404(
                conn,
                self.BASE_QUERY + " WHERE a.asset_id = ?",
                (asset_id,)
            )

    def create(self, data: dict) -> int:
        with get_db() as conn:
            cursor = conn.execute("""
                INSERT INTO assets (title, asset_type_id)
                VALUES (?, ?)
            """, (
                data["title"],
                data["asset_type_id"],
            ))
            conn.commit()
            return cursor.lastrowid

    def update(self, asset_id: int, data: dict) -> None:
        with get_db() as conn:
            conn.execute("""
                UPDATE assets
                SET title = ?,
                    asset_type_id = ?
                WHERE asset_id = ?
            """, (
                data["title"],
                data["asset_type_id"],
                asset_id,
            ))
            conn.commit()

    def delete(self, asset_id: int) -> None:
        with get_db() as conn:
            conn.execute(
                "DELETE FROM assets WHERE asset_id = ?",
                (asset_id,)
            )
            conn.commit()