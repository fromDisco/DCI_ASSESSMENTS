Some helpful instructions:

In this exercise, explore the use of iPython. A tool for interactive computing.

Start the iPython shell by typing the following command:

```console
ipython
```

You can load scripts in the currently working directory by:

```console
%load <name of file>.py
```

Sometimes when code is loaded you have to press the `enter` key two times for it to be reflected.



# Exercise



- Design a `__repr__` method to return a string that looks like this:

```python
<Reminder id=1, title="XYZ", description="some description">
```

- Design a `find(id)` class method in the `Reminder` class which will work as follows (hint -> `@classmethod`):

```console
x = Reminder.find(1)
print(x)
```

When the instance is printed, it should be represented as:

`<Reminder id=1, title="XYZ", description="some description">`

- Design unit tests for your model methods:

    - `test_find`
    - `test_save`

- Optional: Change the `save()` in such a well that you can return an instance of the class reminder