import os 
import sqlite3
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s' # Change INFO to WARNING to only show warning ansd errors. Or ERROR for only errors.
)
logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Folder where the script lives
DB_PATH = os.path.join(BASE_DIR, 'app.db') # The database file


def create_db():
    logger.info('Creating database')
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create Items Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY, 
        name TEXT NOT NULL,
        item_type TEXT NOT NULL,
        strength TEXT NOT NULL,
        description TEXT, 
        value INTEGER NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()
    logger.info('Database created')
    print("Database created!")


def safe_create_db():
    error = None
    try:
        create_db()
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
    delete_db(safe_mode=True)
    safe_create_db()


if __name__ == "__main__":
    reset_db()