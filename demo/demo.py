from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger(__name__)

DB_PATH = Path(__file__).resolve().parent / 'app.db'

def demo():
    if not DB_PATH.exists():
        logger.info('Database does not exist')
        return 'DATABASE DOES NOT EXIST'

if __name__ == '__main__':
    if not DB_PATH.exists():
        print('Database does not exist')
        