"""
Application configuration module.

This file centralises all configuration logic for the backend application,
including environment variables, database paths, and shared settings.

Purpose:
- Provide a single source of truth for configuration values
- Improve maintainability and scalability
- Avoid hardcoding values across the codebase

Typical usage:
- Load environment variables (.env)
- Define database connection paths/URLs
- Store global constants used across the application

Example:
    from backend.core.config import settings
    db_path = settings.DB_PATH
"""