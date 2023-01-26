#!/usr/bin/env python

####################################################################
#         DO NOT TOUCH OR CHANGE ANYTHING IN THIS FILE             #
####################################################################


from animal import Animal
from dog import Dog
from german_shepherd import GermanShepherd


def main():
    # Behavior of a human.
    human = Animal(2, 2)
    human.summary()
    print()
    human.breathe()
    print()
    human.walk()
    print("=====")

    # Behavior of a dog
    dog = Dog()
    dog.summary()
    print()
    dog.breathe()
    print()
    dog.walk()
    print("=====")

    # Behavior of a German Shepard
    german_shepard = GermanShepherd()
    german_shepard.summary()
    print()
    german_shepard.breathe()
    print()
    german_shepard.walk()
    print("=====")


if __name__ == "__main__":
    main()
