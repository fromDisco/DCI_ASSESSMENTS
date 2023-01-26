import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from .connect import Connect


def db_drop_create(query):
    """
    If DB ist existent, delete it
    """
    config = {
        "user": "postgres",
        "password": "postgres",
        "host": "localhost",
        "port": "5432",
    }

    # get connection
    connect = Connect(config)
    connection = connect.connection

    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connect.cursor
    cursor.execute(query)
    connection.commit()

    # close connection
    connect.closing(connection, cursor)


def db_populate(query):
    """
    Populate database with data for testing purpose
    """
    config = {
        "user": "postgres",
        "password": "postgres",
        "host": "localhost",
        "port": "5432",
        "database": "flask_intro_test",
    }
    connect = Connect(config)
    connection = connect.connection

    # connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connect.cursor
    cursor.execute(query)
    connection.commit()

    # close connection
    connect.closing(connection, cursor)
