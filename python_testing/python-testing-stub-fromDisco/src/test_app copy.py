import unittest
from unittest import mock
import os
import json
import app

class SchedulerTest(unittest.TestCase):

    #@mock.patch("app.HamburgRailExchangeScheduler.get_city_data")
    @mock.patch("app.HamburgRailExchangeScheduler.get_city_data")
    def setUp(self, mock_rail_city_data):
        """
        Get data from json files

        Mock methods of HamburgRailExchangeScheduler that make
        url requests.
        Stub data of the methods.
        """
        # read actual file path
        file_path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(file_path)

        # navigate to data folder and read file list
        os.chdir("../data")
        folder_content = os.listdir()

        # read content of files and add them to dictionary
        self.cities_data = {}
        for file in folder_content:
            city = file.split(".")[0]
            with open(file) as city_data:
                self.cities_data[city] = json.load(city_data)
        
        # mock_return = mock.MagicMock()
        # mock_return.return_value = self.cities_data
        # mock_rail_city_data.return_value = mock_return()

        # mock get_city_data return with fake data
        mock_rail_city_data.return_value = self.cities_data

        # instantiate the real Class
        self.object = app.HamburgRailExchangeScheduler()

    def test_run(self):
        self.object.schedule_train_to_hamburg("bremen", "01:11")


if __name__ == "__main__":
    unittest.main()
