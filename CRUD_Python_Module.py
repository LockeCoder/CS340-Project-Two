# CRUD_Python_Module.py
from typing import Dict, List
from urllib.parse import quote_plus

from pymongo import MongoClient
from pymongo.errors import PyMongoError, ServerSelectionTimeoutError


class AnimalShelter:
    """
    CRUD operations for the 'animals' collection in the 'aac' database.

    Public API:
        - create(data) -> bool
        - read(query) -> list
        - update(filter, new_values) -> int
        - delete(filter) -> int
    """

    def __init__(
        self,
        username: str,
        password: str,
        host: str = "localhost",
        port: int = 27017,
        db_name: str = "aac",
        col_name: str = "animals",
        server_timeout_ms: int = 5000,
        auth_source: str = "admin",  
    ):
        """
        If username/password are provided, connect with auth; otherwise connect unauthenticated
        (useful if mongod is running without access control in a local lab).
        """
        if username and password:
            u = quote_plus(username)
            p = quote_plus(password)
            uri = f"mongodb://{u}:{p}@{host}:{port}"
            self.client = MongoClient(
                uri,
                authSource=auth_source,                 
                serverSelectionTimeoutMS=server_timeout_ms,
            )
        else:
            self.client = MongoClient(
                f"mongodb://{host}:{port}",
                serverSelectionTimeoutMS=server_timeout_ms,
            )

        self.database = self.client[db_name]
        self.collection = self.database[col_name]

        # Health check so bad creds show up immediately
        try:
            self.client.admin.command("ping")
        except ServerSelectionTimeoutError as e:
            raise RuntimeError(f"Cannot reach MongoDB at {host}:{port}: {e}") from e
        except PyMongoError as e:
            raise RuntimeError(f"MongoDB auth/connection failed: {e}") from e

    # CRUD 
    def create(self, data: Dict) -> bool:
        """Insert one document. Return True on success, else False."""
        if not isinstance(data, dict) or not data:
            return False
        try:
            result = self.collection.insert_one(data)
            return bool(result.inserted_id)
        except PyMongoError:
            return False

    def read(self, query: Dict) -> List[Dict]:
        """Return list of documents matching query (empty list if none or on error)."""
        if not isinstance(query, dict):
            return []
        try:
            cursor = self.collection.find(query, {"_id": 0})
            return list(cursor)
        except PyMongoError:
            return []

    def update(self, filter: Dict, new_values: Dict) -> int:
        """Update documents; return number modified (0 on error)."""
        if not isinstance(filter, dict) or not isinstance(new_values, dict):
            return 0
        try:
            res = self.collection.update_many(filter, new_values)
            return int(res.modified_count)
        except PyMongoError:
            return 0

    def delete(self, filter: Dict) -> int:
        """Delete documents; return number removed (0 on error)."""
        if not isinstance(filter, dict):
            return 0
        try:
            res = self.collection.delete_many(filter)
            return int(res.deleted_count)
        except PyMongoError:
            return 0