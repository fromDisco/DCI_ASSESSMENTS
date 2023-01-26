import unittest
from unittest.mock import patch

from .db_setup import db_drop_create, db_populate
from ..app.models import Reminder
from .. import app


class TestApp(unittest.TestCase):
    def setUp(self):
        # Used for patching: database parameters
        self.config_populate = {
            "user": "postgres",
            "password": "postgres",
            "host": "localhost",
            "port": "5432",
            "database": "flask_intro_test",
        }

        # create and polulate a fresh database
        db_drop_create("DROP DATABASE IF EXISTS flask_intro_test")
        db_drop_create("CREATE DATABASE flask_intro_test")
        db_populate(
            """CREATE TABLE reminders (id SERIAL PRIMARY KEY,
            title VARCHAR(255), description TEXT)"""
        )
        db_populate(
            """INSERT INTO reminders (title, description) VALUES('Mirjam is awesome',
            'She is learning to code'),
            ('Eat', 'Food is healthy'),
            ('Exercise', 'Get your heart moving');"""
        )

    def test_find(self):
        test_string = "<Reminder id=1, title=Mirjam is awesome, description=She is learning to code>"
        self.assertEqual(str(Reminder.find(1)), test_string)

    def test_save(self):
        test_obj = Reminder("Herr", "von Boedefeld")
        test_string = "<Reminder id=4, title=Herr, description=von Boedefeld>"

        # patch database config in module that is tested
        with patch.dict(app.models.config, self.config_populate):
            self.assertEqual(str(test_obj.save()), test_string)

    def tearDown(self):
        # after testing: drop test_database
        db_drop_create("DROP DATABASE IF EXISTS flask_intro_test")


if __name__ == "__main__":
    unittest.main()
