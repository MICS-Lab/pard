from pard.koshi_goldstein import koshi_goldstein


def test_koshi_goldstein() -> None:
    # # Symmetric tests
    # assert koshi_goldstein("C", "W", True, warning=False) == (2*139+11*137)/(2+11)
    # assert koshi_goldstein("W", "C", True, warning=False) == (2*139+11*137)/(2+11)
    #
    # assert koshi_goldstein("W", "I", True, warning=False) == 73  # None ting
    # assert koshi_goldstein("I", "W", True, warning=False) == 73  # None ting
    #
    # assert koshi_goldstein("N", "N", True, warning=False) == 0
    # assert koshi_goldstein("I", "I", True, warning=False) == 0
    # assert koshi_goldstein("L", "L", True, warning=False) == 0
    # assert koshi_goldstein("M", "M", True, warning=False) == 0
    # assert koshi_goldstein("W", "W", True, warning=False) == 0
    # assert koshi_goldstein("H", "H", True, warning=False) == 0
    # assert koshi_goldstein("His", "His", True, warning=False) == 0
    #
    # # Asymmetric tests
    # assert koshi_goldstein("C", "W", False, warning=False) == 139
    # assert koshi_goldstein("Cys", "Trp", False, warning=False) == 139
    # assert koshi_goldstein("cys", "trp", False, warning=False) == 139
    # assert koshi_goldstein("W", "C", False, warning=False) == 137
    # assert koshi_goldstein("TRP", "CYS", False, warning=False) == 137
    # assert koshi_goldstein("W", "CYS", False, warning=False) == 137
    #
    # assert koshi_goldstein("W", "I", False, warning=False) is None
    # assert koshi_goldstein("I", "W", False, warning=False) == 73
    #
    # assert koshi_goldstein("N", "N", False, warning=False) == 0
    # assert koshi_goldstein("I", "I", False, warning=False) == 0
    # assert koshi_goldstein("L", "L", False, warning=False) == 0
    # assert koshi_goldstein("M", "M", False, warning=False) == 0
    # assert koshi_goldstein("W", "W", False, warning=False) == 0
    # assert koshi_goldstein("H", "H", False, warning=False) == 0
    # assert koshi_goldstein("His", "His", False, warning=False) == 0

    # With warning; run still goes through
    assert koshi_goldstein("-", "-", False, warning=True) == 60.2
    assert koshi_goldstein("A", "A", False, warning=True) == 51.3
    assert koshi_goldstein("Ala", "Ala", False, warning=True) == 51.3
    # assert koshi_goldstein("-", "-", True, warning=True) == 60.2
    # assert koshi_goldstein("A", "A", True, warning=True) == 51.3
    # assert koshi_goldstein("Ala", "Ala", True, warning=True) == 51.3
