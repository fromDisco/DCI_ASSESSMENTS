# the main part of the code is from
# https://www.postgresqltutorial.com/postgresql-python/connect/
# parts are rewritten
import psycopg2
from config import config
import time


class Connect:
    def __init__(self):
        self.connection, self.cursor = self.establish_connection()

    def establish_connection(self):
        """Connect to the PostgreSQL database server"""
        connection = None
        # read connection parameters
        params = config()
        while connection == None:
            try:
                # waiting for the database to connect
                # connect to the PostgreSQL server
                # print("Connecting to the PostgreSQL database...")
                connection = psycopg2.connect(**params)
                # connection.close()

                # create a cursor
                cursor = connection.cursor()

                # execute a statement
                # print('PostgreSQL database version:')
                cursor.execute("SELECT version()")

                return connection, cursor

            except (
                Exception,
                psycopg2.DatabaseError,
                psycopg2.OperationalError,
            ) as error:
                print(error)
                print("waiting ...")

        # print("Connection established.")

    def closing(self, connection, cursor):
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
            # print("Database connection closed.")
