# Unittest basic 1


## Task1

Write a test in `src/test.py` to check if the function `to_upper` in `src/text.py` will return the `"ABCDEF"` when called with the argument "abcdef".

## Task2

Write a test in `src/test.py` to check if the function `to_word_list_isupper` in `src/text.py` will return `True` when called with the argument `['I', 'LOVE', 'YOU']`.

## Task3

Write a test in `src/test.py` to check if the function `to_word_list_isupper` in `src/text.py` will return `False` when called with the argument `['i', 'LOVE', 'YOU']`.

## Task4

Write a test in `src/test.py` to check if the function `to_upper` in `src/text.py` will raise a **TypeError** if called with an argument that is not a string (**str**).

## Task5

Write a test in `src/test.py` to check if the function `to_word_list_isupper` in `src/text.py` will raise a **TypeError** if called with an argument that is not a **list**.

## Task6

Fix both functions **to_upper** and **to_word_list_isupper** in `src/text.py` so they will raise a **TypeError** if the argument was not the right type (**string** in the case of `to_upper` and **list** in the case of `to_word_list_upper`).


## Objectives:
- Learn about assertEqual.
- Learn about assertTrue.
- Learn about assertFalse.
- Learn about assertRaises.

> **Hint:** Run the tests by executing:

    python3 test.py

> Or run the test with more details by executing:

    python3 -m unittest -v test.py
