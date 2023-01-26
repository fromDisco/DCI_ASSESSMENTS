import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# DO NOT CHANGE THIS FILE


def connect_db():
    uri = os.environ.get(
        "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/tdd_test"
    )
    connection = psycopg2.connect(uri)
    cur = connection.cursor()
    return connection, cur


def save_to_db(connection):
    """
    Save any changes and make them persist to the database.
    """
    connection.commit()
    print("Any changes have been saved to table")


def close_connection(connection, cursor):
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Database connection closed")
