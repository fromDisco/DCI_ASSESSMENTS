from connect import Connect
from helpers import query_parser, add_to_db
from solution_2 import get_employee_detail


def update_employee_experience(employee_id):
    """
    Get complete data from one employee
    """

    sql_string = f"update employee SET experience = (select EXTRACT(YEAR FROM (AGE(current_date, joining_date))) From employee where id = {employee_id}) where id = {employee_id};"

    # call database updating function
    add_to_db(sql_string)

    # call database reading function to get updated user
    output = get_employee_detail(employee_id)

    return output
