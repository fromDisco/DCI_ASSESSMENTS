class MathematicalError(Exception):
    pass


class Calculator:
    def __init__(self, user_input: str):
        self.operators = ["+", "-", "/", "*"]
        self.n1, self.op, self.n2 = self.parse_input(user_input)

    def parse_input(self, user_input: str) -> tuple:
        """
        Split user string. Check for wrong inputs.
        Convert numbers to int.
        """
        elements = user_input.split()

        if len(elements) != 3:
            raise MathematicalError("Input does not consist of three elements")

        if not elements[0].isdigit() or not elements[2].isdigit():
            raise MathematicalError("The first and third input value must be numbers")

        if elements[1] not in self.operators:
            raise MathematicalError('Invalid operator. Can only use "+" or "-"')

        if elements[0] == 0 and elements[1] == "/":
            raise MathematicalError("Devision through 0 is not possible")

        n1 = int(elements[0])
        op = elements[1]
        n2 = int(elements[2])

        return n1, op, n2

    def calculate(self):
        """
        Calculate user input
        """
        if self.op == "+":
            return self.n1 + self.n2
        if self.op == "-":
            return self.n1 - self.n2
        if self.op == "*":
            return self.n1 * self.n2
        if self.op == "/":
            return self.n1 / self.n2


if __name__ == "__main__":

    while True:
        user_input = input(">>> ")
        if user_input == "quit":
            break
        calculator = Calculator(user_input)
        result = calculator.calculate()
        print(result)
