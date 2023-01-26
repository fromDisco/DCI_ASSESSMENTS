from connect import Connect
from helpers import query_parser, read_from_db


def get_employee_detail(num: int) -> str:
    """
    Get complete data from one employee
    """

    sql_string = f"SELECT * FROM employee WHERE id = {num};"
    # call database reading function to get user
    employee_tuple = read_from_db(sql_string)

    return employee_tuple


def get_warehouse_detail(num: int) -> str:
    """
    Get complete data from one warehouse
    """

    sql_string = f"SELECT * FROM warehouse WHERE id = {num};"
    warehouse_tuple = read_from_db(sql_string)

    return warehouse_tuple
