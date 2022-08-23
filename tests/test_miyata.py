from pard.miyata import miyata


def test_miyata() -> None:
    assert miyata("C", "W") == 3.34
    assert miyata("Cys", "Trp") == 3.34
    assert miyata("cys", "trp") == 3.34
    assert miyata("C", "trp") == 3.34
    assert miyata("W", "C") == 3.34
    assert miyata("Trp", "Cys") == 3.34
    assert miyata("TRP", "CYS") == 3.34
    assert miyata("W", "CYS") == 3.34

    assert miyata("W", "I") == 1.72
    assert miyata("I", "W") == 1.72

    assert miyata("W", "L") == 1.73
    assert miyata("L", "W") == 1.73

    assert miyata("M", "W") == 1.89
    assert miyata("W", "M") == 1.89

    assert miyata("Y", "W") == 1.06
    assert miyata("W", "Y") == 1.06

    assert miyata("N", "N") == 0
    assert miyata("I", "I") == 0
    assert miyata("L", "L") == 0
    assert miyata("M", "M") == 0
    assert miyata("W", "W") == 0
    assert miyata("H", "H") == 0
    assert miyata("His", "His") == 0
