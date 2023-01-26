from author import Author
from gender import Gender


class Book(Author):
    def __init__(self, name: str, author: Author, price: float, qty: int):
        self._name = name
        self._author = author
        self._price = price
        self._qty = qty

    def get_name(self) -> str:
        return self._name

    def get_author(self) -> str:
        return self._author

    def get_author_name(self) -> str:
        return self._author.get_name()

    def get_author_email(self) -> str:
        return self._author.get_email()

    def get_price(self) -> float:
        return self._price

    def set_price(self, price: float) -> None:
        self._price = price

    def get_qty(self) -> int:
        return self._qty

    def set_qty(self, qty: int) -> None:
        self._qty = qty

    def __str__(self) -> str:
        return f"Book[name={self.get_name()}, {self.get_author()}, price={self.get_price()}, qty={self.get_qty()}]"


# author1 = Author("Gabriel", "gabriel@email.com", Gender.MALE.value)
# author2 = Author("Lara", "lara@email.com", Gender.FEMALE.value)
# author3 = Author("Joan", "joan@email.com", Gender.OTHER.value)
# book = Book("How to Construct a New Society", author3, 13.50, 20)
# print(book)
