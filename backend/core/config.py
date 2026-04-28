"""
Application settings module.
Handles environments variables and shard settings.
"""

import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Settings:
    """Centralised settings class"""

    DB_PATH = os.path.join(BASE_DIR, 'backend', 'database', 'app.db')
    ENV = os.getenv('ENV', 'development')
    API_URL = os.getenv('API_URL', 'http://localhost:8000')

settings = Settings()