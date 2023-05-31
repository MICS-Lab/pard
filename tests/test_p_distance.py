from pard.pairwise_distance import p_distance

def test_p_distance() -> None:
    assert p_distance('A', 'A') == 0

    assert p_distance("L", "I") == 1
    assert p_distance("Leu", "Ile") == 1
    assert p_distance("leu", "ile") == 1
    assert p_distance("L", "ile") == 1
    assert p_distance("I", "L") == 1
    assert p_distance("Ile", "Leu") == 1
    assert p_distance("ILE", "LEU") == 1
    assert p_distance("ILE", "L") == 1

    assert p_distance("N", "I") == 1
    assert p_distance("I", "N") == 1

    assert p_distance("N", "L") == 1
    assert p_distance("L", "N") == 1

    assert p_distance("M", "W") == 1
    assert p_distance("W", "M") == 1

    assert p_distance("L", "W") == 1
    assert p_distance("W", "L") == 1

    assert p_distance("N", "N") == 0
    assert p_distance("I", "I") == 0
    assert p_distance("L", "L") == 0
    assert p_distance("M", "M") == 0
    assert p_distance("W", "W") == 0
    assert p_distance("H", "H") == 0
    assert p_distance("His", "His") == 0
