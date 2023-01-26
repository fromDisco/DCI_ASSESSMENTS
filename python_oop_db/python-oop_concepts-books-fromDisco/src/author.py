from gender import Gender
from typing import Final


class Author:
    def __init__(self, name: str, email: str, gender: str):
        self._name: Final = name
        self._email = email
        self._gender: Final = Gender(gender)

    def get_name(self) -> str:
        return self._name

    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str) -> str:
        self._email = email

    def get_gender(self) -> str:
        return self._gender.value

    def __str__(self) -> str:
        return f"Author[name={self.get_name()}, email={self.get_email()}, gender={self.get_gender()}]"
