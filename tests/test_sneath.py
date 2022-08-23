from pard.sneath import sneath


def test_sneath() -> None:
    assert sneath("L", "I") == 5
    assert sneath("I", "L") == 5

    assert sneath("N", "I") == 23
    assert sneath("I", "N") == 23

    assert sneath("N", "L") == 20
    assert sneath("L", "N") == 20

    assert sneath("M", "W") == 31
    assert sneath("Met", "Trp") == 31
    assert sneath("W", "M") == 31
    assert sneath("TRP", "M") == 31

    assert sneath("L", "W") == 30
    assert sneath("W", "L") == 30

    assert sneath("N", "N") == 0
    assert sneath("I", "I") == 0
    assert sneath("L", "L") == 0
    assert sneath("M", "M") == 0
    assert sneath("W", "W") == 0
    assert sneath("H", "H") == 0
    assert sneath("His", "His") == 0
