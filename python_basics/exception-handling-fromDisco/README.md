# Python basics - Exceptions III

## Reading material on exceptions

https://docs.python.org/3/tutorial/errors.html 

## Coding a calculator

### Context

In this exercise, your are given code for a program that is a basic calculator. User input is assumed to be a mathematical formula that consist of a number, an operator (at least + and -), and another number, **separated by white space** (e.g. 1 + 1). Here is the basic code for the calculator:


Create a new exception class called "MathematicalError" from BaseException class

```python
class MathematicalError(Exception):pass
```

Create a Calculator class that has the following methods:

`parse_input` that parses all the user input according to rules list defined in the exercise text. Hint: You can run this in your `__init__` (constructor function).

```python
def parse_input(self, user_input):
```


Create another class method called `calculate` that uses the parsed values that are stored as instance private instance variables `self.n1`, `self.op`, and `self.n2`

```python
def calculate(self):

  if self.op == '+':
    return self.n1 + self.n2
  if self.op == '-':
    return self.n1 - self.n2
  if self.op == '*':
    return self.n1 * self.n2
  if self.op == '/':
    return self.n1 / self.n2
```    

To use this, at the bottom of your file add this:

```python
if __name__ == '__main__':
  while True:
    user_input = input('>>> ')
    if user_input == 'quit':
      break
    calculator = Calculator(user_input)
    result = calculator.calculate()
    print(result)
```

An interaction could look like this (easiest if you run this in your Python console:

```python
>>> 1 + 1
2.0
>>> 3.2 - 1.5
1.7000000000000002
>>> quit
```

### Task

Your task is to write a class method called `parse_input`,that splits user input using `str.split()`, and checks (using exceptions) whether the following list of things are valid (using try and except):

1. If the input does not consist of 3 elements, raise a `MathematicalError`, which is a **custom Exception**. **_(Hint: create a custom exception class)_**
2. Try to convert the first and third input to a float type(like so: `float_value = float(str_value))`. Catch any `ValueError`(built-in exception) that occurs, and instead raise a `MathematicalError` (custom exception).
3. If the second input is not '+' or '-' (or any other operator that you use), again raise a `MathematicalError`.

If the input is valid, perform the calculation and print out the result (as in the code above). The user is then prompted to provide new input, and so on, until the user types "quit".

### ```unittest```

In order to test your solution:

1. *Name* your solution file as **calculator.py** .Run the test_calc.py
2. *Run* the **test_calc.py** script.
