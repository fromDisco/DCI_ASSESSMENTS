from dog import Dog


def test_dog():
    # Behavior of a dog
    dog = Dog()
    dog_summary = dog.summary()
    dog_breath = dog.breathe()
    dog_walk = dog.walk()
    assert (
        dog_summary
        == 'This is an instance of ["Dog"]. It has ["4"] legs and ["2"] eyes.'
    )
    assert dog_walk == "Dogs love to run."
    assert dog_breath == "Dogs love to breathe with their mouths open."
