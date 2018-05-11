from peewee import Database
from peewee_moves import DatabaseManager


def get(db: Database) -> DatabaseManager:
    """Get the Database Manager."""
    return DatabaseManager(db)
