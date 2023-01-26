import unittest

# import functions from solutions
from solution_1 import read_database_version
from solution_2 import get_warehouse_detail, get_employee_detail
from solution_3 import update_employee_experience
from solution_4 import get_specialist_employee_list
import datetime


class TestCalcSolution(unittest.TestCase):
    def test_solution_1(self):
        # Add the print statement from your solution 1 to the empty string below
        answer = (
            "PostgreSQL 15.1 (Ubuntu 15.1-1.pgdg20.04+1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0, 64-bit",
        )
        self.assertEqual(read_database_version(), answer)

    def test_solution_2(self):
        self.assertEqual(
            get_employee_detail(105),
            [
                (
                    105,
                    "Linda",
                    3,
                    datetime.date(2004, 6, 4),
                    "Logistics Spcialist",
                    42000,
                    None,
                )
            ],
        )
        self.assertEqual(get_warehouse_detail(2), [(2, "Rewe Warehouse", 400)])

    def test_solution_3(self):
        update_test = [
            (101, "Mo", 1, datetime.date(2005, 2, 10), "HR Manager", 40000, 17)
        ]
        self.assertEqual(update_employee_experience(101), update_test)

    def test_solution_4(self):

        selection_test = [
            (102, "Michael", 1, datetime.date(2018, 7, 23), "Driver", 30000, None),
            (108, "Karen", 4, datetime.date(2011, 10, 17), "Driver", 30000, None),
        ]
        # Add the print statements from your solution 4 to the empty string below
        self.assertEqual(get_specialist_employee_list("Driver", 30000), selection_test)
