from text import to_upper, to_word_list_isupper
import unittest


class Test_Text(unittest.TestCase):
    def test_to_upper(self):
        """
        Checks if given string is converted to uppercase
        """
        test_func = to_upper("abcdef")
        expected_output = "ABCDEF"
        self.assertEqual(test_func, expected_output)

    def test_to_upper_type_error(self):
        """
        Checks if TypeError is raised if argument is not a string
        """
        test_arg = 9

        with self.assertRaises(TypeError):
            to_upper(test_arg)

    def test_to_word_list_isupper(self):
        """
        Checks if to_word_list_isupper checks for uppercase correctly
        """
        test_arg = to_word_list_isupper(["I", "LOVE", "YOU"])
        self.assertTrue(test_arg)

    def test_to_word_list_is_not_upper(self):
        """
        Checks if to_word_list_isupper repeats false if string is not upper
        """
        test_wrong = to_word_list_isupper(["i", "LOVE", "YOU"])
        self.assertFalse(test_wrong)

    def test_list_type_error(self):
        """
        checks if to_word_list_isupper raises TypeError
        """
        test_arg = 9
        with self.assertRaises(TypeError):
            to_word_list_isupper(test_arg)


if __name__ == "__main__":
    unittest.main()
