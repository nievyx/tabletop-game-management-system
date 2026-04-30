import sqlite3
import os
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'backend', 'database', 'app.db')
BACKUP_DIR = os.path.join(BASE_DIR, 'backups')


def backup_sqlite_db():
    """
    Creates a timestamped backup of the SQLITE database
    using the official SQLite backup API
    """

    if not os.path.isfile(DB_PATH):
        print(f'FAILED: Database not found at {DB_PATH}')
        return None

    os.makedirs(BACKUP_DIR, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(
        BACKUP_DIR,
        f'app_{timestamp}.db'
        )

    try:
        source = sqlite3.connect(DB_PATH)
        dest = sqlite3.connect(backup_path)

        with dest:
            source.backup(dest)
        
        source.close()
        dest.close()

        print(f'SUCCESS: backup created at {backup_path}')
        return backup_path

    except Exception as e:
        print(f'FAILED: Backup error: {str(e)}')
        return None

if __name__ == '__main__':
    try:
        result = backup_sqlite_db()

        if result:
            print('Process completed successfully')
        else:
            print('Process failed.')
    
    except ImportError:
        print('ERR: could not find imports')
    except Exception as e:
        print(f'CRITICAL ERROR: {str(e)}')


