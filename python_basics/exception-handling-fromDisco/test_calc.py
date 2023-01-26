from calculator import MathematicalError, Calculator
import unittest


input_values_1 = "2 +"
input_values_2 = "a + b"
input_values_3 = "2 # 2"


class TestCalcSolution(unittest.TestCase):
    def test_calculator_1(self):

        with self.assertRaises(MathematicalError) as context:
            Calculator(input_values_1)
        self.assertEqual(
            str(context.exception), "Input does not consist of three elements"
        )

    def test_calculator_2(self):
        with self.assertRaises(MathematicalError) as context:
            Calculator(input_values_2)
        self.assertEqual(
            str(context.exception), "The first and third input value must be numbers"
        )

    def test_calculator_3(self):
        with self.assertRaises(MathematicalError) as context:
            Calculator(input_values_3)
        self.assertEqual(
            str(context.exception), 'Invalid operator. Can only use "+" or "-"'
        )

    def test_calculator(self):
        calculator = Calculator("1 + 1")
        self.assertEqual(calculator.calculate(), 2.0)


if __name__ == "__main__":
    unittest.main()
