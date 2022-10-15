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

    # Asymmetric tests
    assert koshi_goldstein("C", "W", MatrixType.ALL_RESIDUES, False, warning=False) == 0.2
    assert koshi_goldstein("Cys", "Trp", MatrixType.ALL_RESIDUES, False, warning=False) == 0.2
    assert koshi_goldstein("cys", "trp", MatrixType.ALL_RESIDUES, False, warning=False) == 0.2
    assert koshi_goldstein("W", "C", MatrixType.ALL_RESIDUES, False, warning=False) == 0.7
    assert koshi_goldstein("TRP", "CYS", MatrixType.ALL_RESIDUES, False, warning=False) == 0.7
    assert koshi_goldstein("W", "CYS", MatrixType.ALL_RESIDUES, False, warning=False) == 0.7

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
    # With warning; tests still go through?
    # Exposed Residues
    assert koshi_goldstein("-", "-", MatrixType.EXPOSED, False, warning=True) == 60.2
    assert koshi_goldstein("A", "A", MatrixType.EXPOSED, False, warning=True) == 51.3
    assert koshi_goldstein("Ala", "Ala", MatrixType.EXPOSED, False, warning=True) == 51.3
    assert koshi_goldstein("-", "-", MatrixType.EXPOSED, True, warning=True) == 60.2
    assert koshi_goldstein("A", "A", MatrixType.EXPOSED, True, warning=True) == 51.3
    assert koshi_goldstein("Ala", "Ala", MatrixType.EXPOSED, True, warning=True) == 51.3
