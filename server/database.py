"""Module defining class that interacts with sqlite database"""

from sqlite3 import Connection, Error, connect

from logger import logger
from model import CustomerEvent

SQL_TABLE = """
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY,
        resourceType TEXT NOT NULL,
        resourceId INTEGER NOT NULL,
        eventType TEXT NOT NULL,
        triggeredAt DATETIME NOT NULL,
        triggeredBy TEXT NOT NULL
    );
"""

SQL_INSERT = """
        INSERT INTO events (resourceType, resourceId, eventType, triggeredAt, triggeredBy)
        VALUES (?, ?, ?, ?, ?)
"""


class SqliteHandler:
    """Class that interacts with an SQLite database."""

    def __init__(self) -> None:
        self.db_file = "airddm.db"

    def _create_connection(self):
        """Create a connection to the SQLite database.

        Returns:
            Connection: A connection to the SQLite database.
        """
        conn = None
        try:
            conn = connect(self.db_file)
        except Error as e:
            logger.error(e)
        return conn

    def create_table(self, con: Connection):
        """Create the 'events' table in the SQLite database.

        Args:
            con (Connection): A connection to the SQLite database.
        """
        try:
            cursor = con.cursor()
            cursor.execute(SQL_TABLE)
        except Error as e:
            print(e)

    def insert_data(self, event: CustomerEvent):
        """Insert an event into the 'events' table of the SQLite database.

        Args:
            event (CustomerEvent): The event to be inserted into the database.
        """
        conn = self._create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                SQL_INSERT,
                (
                    event.resource_type,
                    event.resource_id,
                    event.event_type,
                    event.triggered_at,
                    event.triggered_by,
                ),
            )
            conn.commit()
