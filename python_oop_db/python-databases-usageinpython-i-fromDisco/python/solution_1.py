from connect import Connect
from helpers import query_parser, read_from_db


def read_database_version():
    sql_string = "SELECT version();"
    database_tuple = read_from_db(sql_string)

    return database_tuple[0]
