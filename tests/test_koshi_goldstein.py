import pytest

from pard.koshi_goldstein import MatrixType, koshi_goldstein


def test_koshi_goldstein_all_residues() -> None:
    """
    Tests the all residues koshi_golstein matrix

    :return: Nothing
    """
    # Symmetric tests
    assert koshi_goldstein("C", "W", MatrixType.ALL_RESIDUES, True, warning=False) == pytest.approx((0.2+0.7)/2)
    assert koshi_goldstein("W", "C", MatrixType.ALL_RESIDUES, True, warning=False) == pytest.approx((0.7+0.2)/2)
    assert koshi_goldstein("R", "W", MatrixType.ALL_RESIDUES, True, warning=False) == pytest.approx((0.3+0.4)/2)
    assert koshi_goldstein("W", "R", MatrixType.ALL_RESIDUES, True, warning=False) == pytest.approx((0.4+0.3)/2)
    assert koshi_goldstein("R", "-", MatrixType.ALL_RESIDUES, True, warning=False) == pytest.approx((11.3+2.0)/2)
    assert koshi_goldstein("-", "R", MatrixType.ALL_RESIDUES, True, warning=False) == pytest.approx((2.0+11.3)/2)

    # Asymmetric tests
    assert koshi_goldstein("C", "W", MatrixType.ALL_RESIDUES, False, warning=False) == 0.2
    assert koshi_goldstein("Cys", "Trp", MatrixType.ALL_RESIDUES, False, warning=False) == 0.2
    assert koshi_goldstein("cys", "trp", MatrixType.ALL_RESIDUES, False, warning=False) == 0.2
    assert koshi_goldstein("W", "C", MatrixType.ALL_RESIDUES, False, warning=False) == 0.7
    assert koshi_goldstein("TRP", "CYS", MatrixType.ALL_RESIDUES, False, warning=False) == 0.7
    assert koshi_goldstein("W", "CYS", MatrixType.ALL_RESIDUES, False, warning=False) == 0.7
    assert koshi_goldstein("R", "W", MatrixType.ALL_RESIDUES, False, warning=False) == 0.3
    assert koshi_goldstein("Arg", "Trp", MatrixType.ALL_RESIDUES, False, warning=False) == 0.3
    assert koshi_goldstein("arg", "trp", MatrixType.ALL_RESIDUES, False, warning=False) == 0.3
    assert koshi_goldstein("W", "R", MatrixType.ALL_RESIDUES, False, warning=False) == 0.4
    assert koshi_goldstein("TRP", "ARG", MatrixType.ALL_RESIDUES, False, warning=False) == 0.4
    assert koshi_goldstein("W", "ARG", MatrixType.ALL_RESIDUES, False, warning=False) == 0.4
    assert koshi_goldstein("R", "-", MatrixType.ALL_RESIDUES, False, warning=False) == 11.3
    assert koshi_goldstein("-", "R", MatrixType.ALL_RESIDUES, False, warning=False) == 2.0
    assert koshi_goldstein("A", "L", MatrixType.ALL_RESIDUES, False, warning=False) == 1.6

    # With warning; tests still go through?
    # All Residues
    assert koshi_goldstein("-", "-", MatrixType.ALL_RESIDUES, False, warning=True) == 69.2
    assert koshi_goldstein("A", "A", MatrixType.ALL_RESIDUES, False, warning=True) == 61.9
    assert koshi_goldstein("Ala", "Ala", MatrixType.ALL_RESIDUES, False, warning=True) == 61.9
    assert koshi_goldstein("-", "-", MatrixType.ALL_RESIDUES, True, warning=True) == 69.2
    assert koshi_goldstein("A", "A", MatrixType.ALL_RESIDUES, True, warning=True) == 61.9
    assert koshi_goldstein("Ala", "Ala", MatrixType.ALL_RESIDUES, True, warning=True) == 61.9


def test_koshi_goldstein_exposed_residues() -> None:
    """
    Tests the exposed residues koshi_golstein matrix

    :return: Nothing
    """
    # Symmetric tests
    assert koshi_goldstein("R", "W", MatrixType.EXPOSED, True, warning=False) == pytest.approx((0.6+0.1)/2)
    assert koshi_goldstein("W", "R", MatrixType.EXPOSED, True, warning=False) == pytest.approx((0.1+0.6)/2)
    assert koshi_goldstein("R", "-", MatrixType.EXPOSED, True, warning=False) == pytest.approx((11.4+1.7)/2)
    assert koshi_goldstein("-", "R", MatrixType.EXPOSED, True, warning=False) == pytest.approx((1.7+11.4)/2)

    # Asymmetric tests
    assert koshi_goldstein("R", "W", MatrixType.EXPOSED, False, warning=False) == 0.6
    assert koshi_goldstein("Arg", "Trp", MatrixType.EXPOSED, False, warning=False) == 0.6
    assert koshi_goldstein("arg", "trp", MatrixType.EXPOSED, False, warning=False) == 0.6
    assert koshi_goldstein("W", "R", MatrixType.EXPOSED, False, warning=False) == 0.1
    assert koshi_goldstein("TRP", "ARG", MatrixType.EXPOSED, False, warning=False) == 0.1
    assert koshi_goldstein("W", "ARG", MatrixType.EXPOSED, False, warning=False) == 0.1
    assert koshi_goldstein("R", "-", MatrixType.EXPOSED, False, warning=False) == 11.4
    assert koshi_goldstein("-", "R", MatrixType.EXPOSED, False, warning=False) == 1.7

    # With warning; tests still go through?
    # Exposed Residues
    assert koshi_goldstein("-", "-", MatrixType.EXPOSED, False, warning=True) == 60.2
    assert koshi_goldstein("A", "A", MatrixType.EXPOSED, False, warning=True) == 51.3
    assert koshi_goldstein("Ala", "Ala", MatrixType.EXPOSED, False, warning=True) == 51.3
    assert koshi_goldstein("-", "-", MatrixType.EXPOSED, True, warning=True) == 60.2
    assert koshi_goldstein("A", "A", MatrixType.EXPOSED, True, warning=True) == 51.3
    assert koshi_goldstein("Ala", "Ala", MatrixType.EXPOSED, True, warning=True) == 51.3


def test_koshi_goldstein_buried_residues() -> None:
    """
    Tests the exposed residues koshi_golstein matrix

    :return: Nothing
    """
    # Symmetric tests
    assert koshi_goldstein("A", "-", MatrixType.BURIED, True, warning=False) == pytest.approx((1.0+0.2)/2)
    assert koshi_goldstein("-", "A", MatrixType.BURIED, True, warning=False) == pytest.approx((0.2+1.0)/2)

    # Asymmetric tests
    assert koshi_goldstein("A", "-", MatrixType.BURIED, False, warning=False) == 1.0
    assert koshi_goldstein("-", "A", MatrixType.BURIED, False, warning=False) == 0.2

    # With warning; tests still go through?
    # Exposed Residues
    for symmetric_ in [True, False]:
        assert koshi_goldstein("-", "-", MatrixType.BURIED, symmetric_, warning=True) == 79.2
        assert koshi_goldstein("A", "A", MatrixType.BURIED, symmetric_, warning=True) == 76.3
        assert koshi_goldstein("Ala", "Ala", MatrixType.BURIED, symmetric_, warning=True) == 76.3


def test_koshi_goldstein_coil_residues() -> None:
    """
    Tests the coil residues koshi_golstein matrix

    :return: Nothing
    """
    # Symmetric tests
    assert koshi_goldstein("A", "-", MatrixType.COIL, True, warning=False) == pytest.approx((19.0+3.0)/2)
    assert koshi_goldstein("-", "A", MatrixType.COIL, True, warning=False) == pytest.approx((3.0+19.0)/2)
    assert koshi_goldstein("P", "I", MatrixType.COIL, True, warning=False) == pytest.approx((0.3+0.9)/2)
    assert koshi_goldstein("I", "P", MatrixType.COIL, True, warning=False) == pytest.approx((0.9+0.3)/2)

    # Asymmetric tests
    assert koshi_goldstein("A", "-", MatrixType.COIL, False, warning=False) == 19.0
    assert koshi_goldstein("-", "A", MatrixType.COIL, False, warning=False) == 3.0
    assert koshi_goldstein("P", "I", MatrixType.COIL, False, warning=False) == 0.3
    assert koshi_goldstein("I", "P", MatrixType.COIL, False, warning=False) == 0.9

    # With warning; tests still go through?
    # Exposed Residues
    for symmetric_ in True, False:
        assert koshi_goldstein("-", "-", MatrixType.COIL, symmetric_, warning=True) == 60.6
        assert koshi_goldstein("A", "A", MatrixType.COIL, symmetric_, warning=True) == 55.6
        assert koshi_goldstein("Ala", "Ala", MatrixType.COIL, symmetric_, warning=True) == 55.6


def test_koshi_goldstein_turn_residues() -> None:
    """
    Tests the turn residues koshi_golstein matrix

    :return: Nothing
    """
    # Symmetric tests
    assert koshi_goldstein("A", "-", MatrixType.TURN, True, warning=False) == pytest.approx((15.8+3.1)/2)
    assert koshi_goldstein("-", "A", MatrixType.TURN, True, warning=False) == pytest.approx((3.1+15.8)/2)

    # Asymmetric tests
    assert koshi_goldstein("A", "-", MatrixType.TURN, False, warning=False) == 15.8
    assert koshi_goldstein("-", "A", MatrixType.TURN, False, warning=False) == 3.1

    # With warning; tests still go through?
    # Exposed Residues
    for symmetric_ in True, False:
        assert koshi_goldstein("-", "-", MatrixType.TURN, symmetric_, warning=True) == 74.2
        assert koshi_goldstein("A", "A", MatrixType.TURN, symmetric_, warning=True) == 54.3
        assert koshi_goldstein("Ala", "Ala", MatrixType.TURN, symmetric_, warning=True) == 54.3
        assert koshi_goldstein("R", "R", MatrixType.TURN, symmetric_, warning=True) == 68.1
        assert koshi_goldstein("Arg", "Arg", MatrixType.TURN, symmetric_, warning=True) == 68.1

