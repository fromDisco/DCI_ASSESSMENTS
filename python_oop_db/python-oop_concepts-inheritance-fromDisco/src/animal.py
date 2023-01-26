class Animal:
    def __init__(self, number_of_legs: int, number_of_eyes: int):
        self.number_of_legs = number_of_legs
        self.number_of_eyes = number_of_eyes

    def get_number_of_legs(self):
        return self.number_of_legs

    def get_number_of_eyes(self):
        return self.number_of_eyes

    def breathe(self):
        """
        Support breathing of animal, here we return and print as well.
        """
        return_value = "The " + type(self).__name__ + " is breathing."
        print(return_value)
        return return_value

    def walk(self):
        return_value = "Walking with [" + str(self.get_number_of_legs()) + "] legs."
        print(return_value)
        return return_value

    def summary(self):
        return_value = f'This is an instance of ["{type(self).__name__}"]. It has ["{self.get_number_of_legs()}"] legs and ["{self.get_number_of_eyes()}"] eyes.'
        print(return_value)
        return return_value
