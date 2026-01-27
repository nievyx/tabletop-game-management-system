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

# Legacy Function (from rpg game)
# def create_db():
#     logger.info('Creating database')
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()

#     # Create Items Table
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS items (
#         id INTEGER PRIMARY KEY, 
#         name TEXT NOT NULL,
#         item_type TEXT NOT NULL,
#         strength TEXT NOT NULL,
#         description TEXT, 
#         value INTEGER NOT NULL
#     )
#     ''')
    
#     conn.commit()
#     conn.close()
#     logger.info('Database created')
#     print("Database created!")

def read_sql_file(path: str) -> str:
    if not os.path.exists(path):
        raise FileNotFoundError(f'Missing SQL file: {path}')
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def create_db(conn):
    schema_sql = read_sql_file(SCHEMA_PATH)
    conn.executescript(schema_sql)
    # logger.info('Created database Successfully') #- Shows regardless of whether it worked or not

def seed_db(conn):
    seed_sql = read_sql_file(SEED_PATH)
    conn.executescript(seed_sql)
    # logger.info('Seeded database Successfully') #- Shows regardless of whether it worked or not

def create_and_seed_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA foreign_keys = ON;')
    try:
        create_db(conn)
        seed_db(conn)
        conn.commit()
    finally:
        conn.close()


def safe_create_db():
    error = None
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
    if not os.path.exists(DB_PATH):
        logger.warning('Database does not exist: %s', DB_PATH)
        print(f'⚠{DB_PATH} does not exist')
        return False
    
    if safe_mode and not confirm_delete():
        print('Delete Cancelled.')
        return False
     
    # Delete Database
    os.remove(DB_PATH)
    print(f'{DB_PATH} deleted!')
    return True



def reset_db():
    logger.info('Resetting Database')
    delete_db(safe_mode=False)
    safe_create_db()


if __name__ == "__main__":
    reset_db()