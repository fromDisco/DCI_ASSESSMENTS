# Collections Basics 2

After getting our handy dirty with lists we do another round of exercises, now focusing on dictionaries. We will once again go over how to:

- Create a dictionary with data
- Append, access and remove elements
- Loop over dictionary elements

## Usage

Dictionaries (also called dicts) of course can also be stored in variables. For example let's store fruits, grouped by their color:

```python
fruits = {
  'red': ['apple', 'cherry', 'strawberry'],
  'orange':['orange', 'mango', 'peach'],
  'yellow': ['banana', 'lemon']
}
```

Elements in this dictionary can be accessed by keys which are Strings. For example all red fruits can be accessed using `fruits['red']`. The nested value `apple` could be accessed using `fruits['red'][0]`.

To add an element to or update one in a dictionary you can use the key syntax as well or use the `update` method:

```python
fruits['green'] = ['watermelon']
fruits.update({'green': ['watermelon']})
```

To remove an element from a dictionary one can use the `pop` method with a specified key. For example to remove all yellow fruits:

```python
fruits.pop('yellow')
```

You can also loop over dictionaries like you can loop over lists using the `items` method:

```python
for color, colored_fruits in fruits.items()
  print(color + ' fruits:')
  for fruit in colored_fruits:
    print('- ' + fruit)
```

###

## Tasks

###

### Task 1

Create a variable called `person` which should hold a dictionary. The dictionary should have the key `name` with the value `Bart Simpson` and the key `address` with the value `742 Evergreen Terrace`. Print the name and the address separated by comma to the screen.

- Your result should look like this:

```
Bart Simpson, 742 Evergreen Terrace
```

###

### Task 2

Create two variables one called `bart` and the other called `homer`. Each stores a dictionary, one with the key `name` and the value `Bart Simpson`, the other one with the same key but the value `Homer Simpson`. Create a third variable `address` with a dictionary which only has one key `address`.

Use `update` to add the address to both `bart` and `homer`. Print `bart['address']` to the screen.

- Your result should look like this:

```
742 Evergreen Terrace
```

###

### Task 3

Create a variable `ages` which holds a dictionary with the key `Peter` and the value `36`, the key `Robin` and the value `29` and the key `Michael` with the value `33`. Loop over the dictionary and print the name with the age.

- Your result should look like this:

```
Peter is 36 years old
Robin is 29 years old
Michael is 33 years old
```

###

### Task 4

Store the animals `Alligator`, `Tiger`, `Parrot`, `Hamster`, and `Dolphin` as keys in a dict. Use random numbers as values. Now remove all keys ending with `r` from the dictionary and print the resulting dict to the screen.

- Your result should look similar to this:

```
{'Dolphin': 8, 'Parrot': 2}
```
