from pard.grantham import grantham


def test_grantham() -> None:
    assert grantham("L", "I") == 5
    assert grantham("I", "L") == 5

    assert grantham("N", "I") == 149
    assert grantham("I", "N") == 149

    assert grantham("N", "L") == 153
    assert grantham("L", "N") == 153

    assert grantham("M", "W") == 67
    assert grantham("W", "M") == 67

    assert grantham("L", "W") == 61
    assert grantham("W", "L") == 61

    assert grantham("N", "N") == 0
    assert grantham("I", "I") == 0
    assert grantham("L", "L") == 0
    assert grantham("M", "M") == 0
    assert grantham("W", "W") == 0
    assert grantham("H", "H") == 0
