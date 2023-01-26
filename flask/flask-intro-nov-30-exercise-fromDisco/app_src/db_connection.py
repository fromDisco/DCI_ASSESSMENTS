import os
import psycopg2


def make_connection(database_name="flask_intro"):
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    if DATABASE_URL:
        # This is how we shall connect to the CI/CD and future production environments in the Cloud.
        connection = psycopg2.connect(DATABASE_URL)
    else:
        connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432",
            database=database_name,
        )
    connection.autocommit = True
    cursor = connection.cursor()
    return dict(connection=connection, cur=cursor)
