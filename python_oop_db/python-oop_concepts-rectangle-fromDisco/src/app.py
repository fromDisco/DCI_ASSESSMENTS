import math
from check import print_rectangle_properties


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()
        self.diagonal = self.get_diagonal()

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * self.width + 2 * self.height

    def get_width(self) -> float:
        return self.width

    def get_height(self) -> float:
        return self.height

    def get_diagonal(self) -> float:
        return math.sqrt(math.pow(self.width, 2) + math.pow(self.height, 2))
    

  


def main():
    first = Rectangle(9, 12)
    second = Rectangle(17, 13)
    print_rectangle_properties(first)
    print_rectangle_properties(second)


if __name__ == "__main__":
    main()
