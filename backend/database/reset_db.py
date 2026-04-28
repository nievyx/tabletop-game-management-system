import os 
import sqlite3
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s' # Change INFO to WARNING to only show warning ansd errors. Or ERROR for only errors.
)
logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Folder where the script lives
DB_PATH = os.path.join(BASE_DIR, 'app.db') # The database file
SCHEMA_PATH = os.path.join(BASE_DIR, 'schema.sql')
SEED_PATH = os.path.join(BASE_DIR, 'seed.sql')

def read_sql_file(path: str) -> str:
    """
       Reads and returns the contents of a SQL file.

       Args:
           path (str): Path to the SQL file.

       Returns:
           str: SQL script contents.
       """
    if not os.path.exists(path):
        raise FileNotFoundError(f'Missing SQL file: {path}')
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def create_db(conn):
    logger.info('Applying database schema..') 
    schema_sql = read_sql_file(SCHEMA_PATH)
    conn.executescript(schema_sql)

def seed_db(conn):
    logger.info('Applying database seed data..') 
    seed_sql = read_sql_file(SEED_PATH)
    conn.executescript(seed_sql)

def create_and_seed_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA foreign_keys = ON;')
    try:
        create_db(conn)
        seed_db(conn)
        conn.commit()
        logger.info('Database created and seeded successfully')
    finally:
        conn.close()

def safe_create_db():
    try:
        create_and_seed_db()
    except Exception as e:
        print(f'Database creation failed. Error: {e}')


def confirm_delete():
    choice = input(
        f'Database with {DB_PATH} exists. Enter \'yes\' to delete it: '
        )
    return choice.lower() == 'yes'

def delete_db(safe_mode=True):
    """
    Deletes the existing database (if present)

    Args:
        safe_mode (bool, optional): If True, Prompts before deleting database. Defaults to True.

    Returns:
        bool: True if successful, False otherwise
    """
    if not os.path.exists(DB_PATH):
        logger.debug('No existing database found. Skipping delete')
        return False

    if safe_mode and not confirm_delete():
        logger.info('Delete Cancelled.')
        return False

    # Delete Database
    try:
        os.remove(DB_PATH)
        logger.info(f'{DB_PATH} deleted!')
        return True
    except OSError as e:
        logger.error(f'Failed to delete database: {e}')
        return False

def reset_db(safe_mode=True):
    """Deletes the existing database (if present)
    and recreates it using schema and seed SQL data.

    Args:
        safe_mode (bool, optional): If True, Prompts before deleting database. Defaults to True.
    """
    logger.info('Resetting Database')
    delete_db(safe_mode)
    safe_create_db()


if __name__ == "__main__":
    reset_db(safe_mode=False)