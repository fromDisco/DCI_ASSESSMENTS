import unittest
import psycopg2
from models import Reminder, make_connection


# unittest example
class ReminderModel(unittest.TestCase):
    def setUp(self) -> None:
        # drop table and recreate it
        cur = make_connection(database_name="flask_test").get("cur")
        # cur.execute("DROP TABLE IF EXISTS reminders;")
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS reminders (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255),
                description TEXT
            );"""
        )
        reminder = Reminder(title="eat", description="sphagetti and Broccoli")

        # store a sample reminder instance for a later test
        self.reminder = reminder.save()

    def test_save(self):
        # There is no easy way to reset the ID
        # refs: https://brianchildress.co/reset-auto-increment-in-postgres/
        # refs: https://stackoverflow.com/questions/244243/how-to-reset-postgres-primary-key-sequence-when-it-falls-out-of-sync/23390399#23390399
        self.assertEqual(
            f"<Reminder id={self.reminder.id}, title='eat', description='sphagetti and Broccoli'>",
            str(self.reminder),
        )

    def test_find(self):
        reminder = Reminder.find(self.reminder.id)
        self.assertEqual(
            f"<Reminder id={reminder.id}, title='eat', description='sphagetti and Broccoli'>",
            str(reminder),
        )

        self.assertEqual(Reminder.find("a"), None)

    def test_find_many(self):
        """Implement different test cases where you test the exercise"""
        search_for = {"title": "eat", "description": "SPPPPhagetti and Broccoli"}
        reminder = Reminder.find(**search_for)
        self.assertEqual(
            f"<Reminder id={reminder.id}, title='eat', description='sphagetti and Broccoli'>",
            str(reminder),
        )

        self.assertEqual(Reminder.find("a"), None)
