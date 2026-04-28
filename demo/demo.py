from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger(__name__)

DB_PATH = Path(__file__).resolve().parent.parent / 'backend/app/app.db'

def demo():
    if not DB_PATH.exists():
        logger.info("Demo script: database not found (this does not affect API)")
        return 'DATABASE DOES NOT EXIST'
    else:
        logger.info("Demo script: database found (this does not affect API)")
        return 'DATABASE FOUND'

if __name__ == '__main__':
    result = demo()
    print(result)
        