## DO NOT TOUCH THE src/tests folder please.
from gender import Gender
from typing import Final


class Author:
    def __init__(self, name: str, email: str, gender: str):
        self._name: Final = name
        self._email = email
        self._gender: Final = Gender(gender)
## DO NOT MAKE ANY CHANGES TO the animal_reign.py file

## You do not need to create a new file for this exercise. You can work within the boiler plate methods.

## You do not need to change the animal.py file as well (or module)

## Which files do you need to work with today?

- `dog.py`
- `german_shepherd.py`

# Python OOP Concepts - Animal Reign

In this exercise we will check how inheritance in Python and the usage of the **_super()_** built-in method and **_self_** work.

### Installation dependencies

- create a virtual environment
- install dependencies listed in the `requirements.txt` file by doing this:
   
   `pip install -r requirements`

### How to do an automated test on your code (extra test)

Passing this will give you confidence that you will get a human review from your teacher, Victor quickly.

`python -m pytest`

### Overview of animal.py:
- The **_Animal_** class represents an ordinary animal. It contains the _**number_of_legs**_ and the **_number_of_eyes_** 
of an animal, as well as some of its behavior through the methods **_breathe()_** and **_walk()_**.
It also contains the **method _summary()_**, which just summarizes the information of the current animal 
instance.
- No extra action should be taken here.

### Overview of dog.py:
- Since every dog has 4 legs and two eyes, the **constructor** method should make a call to the 
  **Animal** constructor, passing the correspondent values to the constructor.
- You should override the **_breathe()_** method. It should call the **_breathe()_** method of the Animal class and 
  then print `"Dogs love to breathe with their mouths open."`.
- You should override the **_walk()_** method. It should call the **_walk()_** method of the Animal class and then 
  print `"Dogs love to run."`.

### Overview of german_shepard.py:
- You should override the **_walk()_** method. It should call the **_walk()_** method of the Dog class and then
  print ``"German Shepherds show their beautiful fur while running."``.

### Overview of animal_reign.py:
- Where the main method resides, therefore where your code should be executed. An animal (human), a dog and a german 
  shepard instances are created. 
- No extra action should be taken here.


You should have an output similar to the one below:

![img.png](img.png)
