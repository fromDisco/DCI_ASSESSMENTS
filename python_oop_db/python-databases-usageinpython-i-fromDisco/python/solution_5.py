from connect import Connect
from helpers import query_parser, add_to_db


def create_employee(empolyee_sql_query):
    """
    Add a new employee to table employees
    """

    # call database updating function
    add_to_db(empolyee_sql_query)


create_employee(
    "INSERT INTO employee (id, employee_name, warehouse_id, joining_date, speciality, salary, experience) VALUES ('109', 'Olivia', '2', '2021-09-10', 'Consultant', '67500', NULL)"
)
