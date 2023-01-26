from gender import Gender
from author import Author
from book import Book


def test_grading():
    author1 = Author("Gabriel", "gabriel@email.com", Gender.MALE.value)
    author2 = Author("Lara", "lara@email.com", Gender.FEMALE.value)
    author3 = Author("Joan", "joan@email.com", Gender.OTHER.value)
    book = Book("How to Construct a New Society", author3, 13.50, 20)
    assert book.get_name() == "How to Construct a New Society"
    assert author1.get_gender() == "Male"
    assert author2.get_gender() == "Female"
    assert author3.get_gender() == "Other"
    assert author1.get_email() == "gabriel@email.com"
    assert book.get_qty() == 20
    assert book.get_price() == 13.50
