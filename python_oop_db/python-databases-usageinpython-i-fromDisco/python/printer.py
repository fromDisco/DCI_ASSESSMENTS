from solution_1 import read_database_version
from solution_2 import get_warehouse_detail, get_employee_detail
from solution_3 import update_employee_experience
from solution_4 import get_specialist_employee_list
from helpers import query_parser

# SOLUTION 1
print("\nSolution 1:")
print(read_database_version())


# SOLUTION 2
print("\nSolution 2: Read given warehouse and employee details")
warehouse_data = ["Warehouse Id", "Warehouse Name", "Employee Count"]
warehouse_output = "Printing Warehouse record\n"
warehouse_output += query_parser(warehouse_data, get_warehouse_detail(2))
print(warehouse_output)

employee_data = [
    "Employee Id",
    "Employee Name",
    "Warehouse Id",
    "Joining Date",
    "Speciality",
    "Salary",
    "Experience",
]
employee_output = "Printing Employee record\n"
employee_output += query_parser(employee_data, get_employee_detail(105))
print(employee_output)


# SOLUTION 3
print("Solution 3:")
employee_output = "Printing Employee record\n"
employee_output += query_parser(employee_data, update_employee_experience(101))
print(employee_output)

# SOLUTION 4
print("Solution 4:")
specialists = get_specialist_employee_list("Driver", 30000)
employee_output = (
    f"Printing employees whose specialty is Driver and salary greater than 30000\n"
)
employee_output += query_parser(employee_data, specialists)
print(employee_output)
