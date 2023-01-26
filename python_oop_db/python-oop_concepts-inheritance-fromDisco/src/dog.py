from animal import Animal


class Dog(Animal):
    def __init__(self):
        super().__init__(number_of_legs=4, number_of_eyes=2)

    def breathe(self) -> str:
        """
        How does a dog breath
        """
        return_val = "Dogs love to breathe with their mouths open."
        print(return_val)
        return return_val

    def walk(self) -> str:
        """
        How does a dog walk?
        """
        return_val = "Dogs love to run."
        print(return_val)
        return return_val
