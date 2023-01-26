from german_shepherd import GermanShepherd


def test_german_shepherd():
    # Behavior of a German Shepard
    german_shepard = GermanShepherd()
    gs = german_shepard.summary()
    assert (
        gs
        == 'This is an instance of ["GermanShepherd"]. It has ["4"] legs and ["2"] eyes.'
    )
    gb = german_shepard.breathe()
    assert gb == "Dogs love to breathe with their mouths open."
    gw = german_shepard.walk()
    assert gw == "German Shepherds show their beautiful fur while running."
