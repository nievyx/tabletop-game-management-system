from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / 'app.db'


if __name__ == '__main__':
    if not DB_PATH.exists():
        print('Database does not exist')
        