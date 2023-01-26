from animal import Animal


def test_animal():
    human = Animal(2, 2)
    human_summary = human.summary()
    assert (
        human_summary
        == 'This is an instance of ["Animal"]. It has ["2"] legs and ["2"] eyes.'
    )
    breath_string = human.breathe()
    assert breath_string == "The Animal is breathing."
    walk_string = human.walk()
    assert walk_string == "Walking with [2] legs."
