## Test Driven Development Test

### Setup instructions

1) Let's setup the database by running the SQL file `create.sql` using a 
command that looks a lot like this:

`psql < path/to/file -U postgres`

Please note the instructions may vary by operating system. Use the option that has worked for you best.

2) Create a virtual environment and activate it

3) Install the dependencies of Python in this project

```console
pip install -r requirements.txt
```

### How to run your test

`pytest -v` 

>Please note, you are not expected to write code that calls the functions directly in the `classes` or `functions` files. If you do so delete after your quasi tests are completed, reach out to your teacher in case this instruction is not clear. Tests will happen in test files.


### Question 1: Classes [60 points]

*The file `classes.py` has been provided for you.*

A Human class takes in two arguments for its constructor.

e.g. `Human('first name', 'last name')`

The Human class shall have 2 attributes
- last_name
- first_name

An instance method called `save()` has been provided, it is used to  insert data into a table (relation). Return a dictionary instead of a None value. Instructions have been provided in the form of `TODO`. Search for TODO in the code base for fixes.

Recall that to insert data, the following is the code you 
would use:

```sql
INSERT INTO humans (first_name, last_name) values('john', 'doe');
```

For example:

```python
h = Human('John', 'Doe')
return_value = h.save()
print(return_value) 
>>> { "first_name": "John", "last_name": "Doe" }
```


### Question 2: Functions [40 points]

*The file `functions.py` has been provided for you.*

Design a function called `save`, which when given a dictionary with key/value pairs it will store this information in the `humans` table:

```python
{ "first_name": "John", "last_name": "Doe"}
```

Make the test pass by making the save function inside of the `functions.py` module return a dictionary. This will enable the test to pass.

See usage:

```python
>>> save({"first_name": "John", "last_name": "Doe"})
{"id": 1, "first_name": "John", "last_name": "Doe"}
>>>
```

### Hint: What to fix?

Through the code, a comment with the word `TODO` has been provided with hints and some tasks to help you get all 4 tests passing.
Do not forget to `black`en the files so that PEP8 Rules are being observed as much as possible.
