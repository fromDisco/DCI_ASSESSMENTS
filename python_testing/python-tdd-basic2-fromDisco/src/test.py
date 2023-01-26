import unittest
from app import rnd, max_num_in_list


class Test_App(unittest.TestCase):
    # check if max_num_in_list will return right value
    def test_max_num_in_list1(self):
        max_num = max_num_in_list([2, 6, 8, 7, -1])
        expected_result = 8
        error_output = (
            f"return value {max_num} not the greatest value in max_num_in_list"
        )
        self.assertEqual(max_num, expected_result, error_output)

    def test_rnd(self):
        test_list = list(range(2, 21))
        # run test multiple times
        # increases the chance of finding an error
        # but theoretically its possible,
        # that that an error doesn't occure
        # during our test. Its not predictable
        # keeping the randrange small and running it
        # multiple times increases the chance
        # of getting an error a little bit
        for i in range(21):
            test_func = rnd(2, 20)
            self.assertIn(test_func, test_list)

    def test_rnd_range(self):
        # run test multiple times
        # increases the chance of finding an error
        # but theoretically its possible,
        # that that an error doesn't occure
        # during our test. Its not predictable
        # keeping the randrange small and running it
        # multiple times increases the chance
        # of getting an error a little bit
        for _ in range(100):
            rnd_num = rnd(2, 20)
            test_func = 2 <= rnd_num < 21
            error_output = f"{rnd_num} Num is out of range"

            if not test_func:
                self.fail(error_output)


if __name__ == "__main__":
    unittest.main()
