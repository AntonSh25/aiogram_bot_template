from psycopg import AsyncConnection

from app.infrastructure.database.tables.users import _UsersDB


class DB:
    def __init__(self, connection: AsyncConnection) -> None:
        self.users = _UsersDB(connection=connection)
