import unittest
from utils.db import connect_db, save_to_db, close_connection
from functions import save


class HumanTestFunctions(unittest.TestCase):
    def setUp(self):
        connection, cur = connect_db()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS humans (
                id SERIAL PRIMARY KEY,
                first_name TEXT,
                last_name TEXT
            );
        """
        )
        save_to_db(connection)
        close_connection(connection, cur)

    def tearDown(self) -> None:
        connection, cur = connect_db()
        # DELETES the contents of the database table
        cur.execute("DROP TABLE humans;")
        save_to_db(connection)
        close_connection(connection, cur)

    def test_save_human(self):
        h = save({"first_name": "John", "last_name": "Doe"})
        try:
            del h["id"]
        except:
            pass
        assert h == {"first_name": "John", "last_name": "Doe Sr."}
