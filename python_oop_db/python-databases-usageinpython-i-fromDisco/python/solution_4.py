from connect import Connect
from helpers import query_parser, read_from_db


def get_specialist_employee_list(speciality, salary):
    """
    Get complete data from employee with given properties
    """

    sql_string = f"SELECT * FROM employee WHERE salary >= {salary} AND speciality = '{speciality}';"

    # call data getter
    employee_tuple = read_from_db(sql_string)

    return employee_tuple
