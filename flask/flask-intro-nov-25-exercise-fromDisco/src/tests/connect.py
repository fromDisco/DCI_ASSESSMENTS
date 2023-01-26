# the main part of the code is from
# https://www.postgresqltutorial.com/postgresql-python/connect/
# parts are rewritten
import psycopg2
import time


class Connect:
    def __init__(self, config):
        self.config = config
        self.connection, self.cursor = self.establish_connection()

    def establish_connection(self):
        """Connect to the PostgreSQL database server"""
        connection = None
        # read connection parameters
        while connection == None:
            try:
                # waiting for the database to connect
                # connect to the PostgreSQL server
                connection = psycopg2.connect(**self.config)

                # create a cursor
                cursor = connection.cursor()

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
