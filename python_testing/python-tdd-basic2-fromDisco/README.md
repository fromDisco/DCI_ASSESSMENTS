# Unittest Basic 2: More Assert Methods


## Task 1

Write a test to check if the function `rnd` in `src/app.py` will return the correct value given these arguments: `start = 2` and `end = 20`.

## Task 2

Write a test to check if the function `rnd` in `src/app.py` will not return an out-of-range value given these arguments: `start = 2` and `end = 20`.

## Task 3

What problem is there with testing a method that involves randomized value? Can we be sure that the test passes every time when it has passed once? Add a code comment to the tests of task 1 and 2 about any potential issues with those tests.

## Task 4

Fix the function `max_num_in_list` in `src/app.py`. It should return the highest number of the list of numbers given as the argument. That way it will pass the test.



## Objectives:
- Learn about `assertIn`.
- Learn about **passing** commands.
- Learn about **failing** methods.


> **Hint:** Run the tests by executing:

    python3 test.py

> Or run the test with more details by executing:

    python3 -m unittest -v test.py
