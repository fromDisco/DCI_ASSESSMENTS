import unittest
from unittest import mock
import os
import json
import app


class Child_of_RailExchange(app.HamburgRailExchangeScheduler):
    def get_city_data(self):
        # read actual file path
        # just if actual working directory is not the project folder
        file_path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(file_path)

        # navigate to data folder and read file list
        os.chdir("../data")
        folder_content = os.listdir()

        # read content of files and add them to dictionary
        cities_data = {}
        for file in folder_content:
            city = file.split(".")[0]
            with open(file) as city_data:
                cities_data[city] = json.load(city_data)

        return cities_data


class SchedulerTest(unittest.TestCase):

    def setUp(self):
        """
        Get data from json files

        Mock methods of HamburgRailExchangeScheduler that make
        url requests.
        Stub data of the methods.
        """
        self.obj_rail_exchange = Child_of_RailExchange()
        print(self.obj_rail_exchange.get_city_data())
        


    def test_run(self):
        self.obj_rail_exchange.schedule_train_to_hamburg("bremen", "01:11")


if __name__ == "__main__":
    unittest.main()
