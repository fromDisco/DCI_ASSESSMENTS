import unittest
from utils.db import connect_db, save_to_db, close_connection
from classes import Human


class HumanTestClasses(unittest.TestCase):
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

        self.sample_human = Human("Test", "Doe")
        self.sample_human = self.sample_human.save()

    def tearDown(self) -> None:
        connection, cur = connect_db()
        # DELETES the contents of the database table
        cur.execute("DROP TABLE humans;")
        save_to_db(connection)
        close_connection(connection, cur)

    def test_human_get(self):
        h = Human.get(self.sample_human.get("id"))

        assert str(h) == "<Human(first_name=Test, last_name=Doe>"

    def test_human_save(self):
        h = Human("John", "Doe")
        saved_value = h.save()

        self.assertListEqual(
            list(saved_value.keys()), ["id", "first_name", "last_name"]
        )
        del saved_value["id"]

        self.assertDictEqual(
            saved_value,
            {"first_name": "John", "last_name": "Doe"},
            "Dictionaries do not match",
        )

    def test_human_delete(self):
        _id = self.sample_human.get("id")

        # Delete a human
        message = Human.delete(_id)
        assert message == "Successfully deleted human"

        ## confirm if delete happened
        message = Human.get(_id)
        assert message == "Human not found!"

        message = Human.delete(_id)
        assert message == "Human not found!!@$$"


if __name__ == "__main__":
    unittest.main()
