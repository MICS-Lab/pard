from pard.epstein import epstein


def test_epstein() -> None:
    # Symmetric tests
    assert epstein("L", "I", True) == 0
    assert epstein("Leu", "Ile", True) == 0
    assert epstein("leu", "ile", True) == 0
    assert epstein("L", "ile", True) == 0
    assert epstein("I", "L", True) == 0
    assert epstein("Ile", "Leu", True) == 0
    assert epstein("ILE", "LEU", True) == 0
    assert epstein("ILE", "L", True) == 0

    assert epstein("N", "I", True) == 1
    assert epstein("Asn", "Ile", True) == 1
    assert epstein("asn", "ile", True) == 1
    assert epstein("I", "N", True) == 1
    assert epstein("Ile", "Asn", True) == 1
    assert epstein("ILE", "ASN", True) == 1

    assert epstein("N", "L", True) == 1
    assert epstein("L", "N", True) == 1

    assert epstein("W", "M", True) == (0.24+0.32)/2
    assert epstein("M", "W", True) == (0.24+0.32)/2

    assert epstein("A", "T", True) == (0.41+0.40)/2
    assert epstein("T", "A", True) == (0.41+0.40)/2

    assert epstein("N", "N", True) == 0
    assert epstein("I", "I", True) == 0
    assert epstein("L", "L", True) == 0
    assert epstein("M", "M", True) == 0
    assert epstein("W", "W", True) == 0
    assert epstein("H", "H", True) == 0
    assert epstein("His", "His", True) == 0

    # Asymmetric tests
    assert epstein("L", "I", False) == 0
    assert epstein("I", "L", False) == 0

    assert epstein("N", "I", False) == 1
    assert epstein("I", "N", False) == 1

    assert epstein("N", "L", False) == 1
    assert epstein("L", "N", False) == 1

    assert epstein("W", "M", False) == 0.24
    assert epstein("M", "W", False) == 0.32

    assert epstein("A", "T", False) == 0.41
    assert epstein("T", "A", False) == 0.40

    assert epstein("N", "N", False) == 0
    assert epstein("I", "I", False) == 0
    assert epstein("L", "L", False) == 0
    assert epstein("M", "M", False) == 0
    assert epstein("W", "W", False) == 0
    assert epstein("H", "H", False) == 0
    assert epstein("His", "His", False) == 0
