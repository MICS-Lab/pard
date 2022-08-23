from pard.experimental_exchangeability import experimental_exchangeability


def test_experimental_exchangeability() -> None:
    # Symmetric tests
    assert experimental_exchangeability("C", "W", True, warning=False) == (2*139+11*137)/(2+11)
    assert experimental_exchangeability("W", "C", True, warning=False) == (2*139+11*137)/(2+11)

    assert experimental_exchangeability("W", "I", True, warning=False) == 73  # None ting
    assert experimental_exchangeability("I", "W", True, warning=False) == 73  # None ting

    assert experimental_exchangeability("N", "N", True, warning=False) == 0
    assert experimental_exchangeability("I", "I", True, warning=False) == 0
    assert experimental_exchangeability("L", "L", True, warning=False) == 0
    assert experimental_exchangeability("M", "M", True, warning=False) == 0
    assert experimental_exchangeability("W", "W", True, warning=False) == 0
    assert experimental_exchangeability("H", "H", True, warning=False) == 0

    # Asymmetric tests
    assert experimental_exchangeability("C", "W", False, warning=False) == 139
    assert experimental_exchangeability("W", "C", False, warning=False) == 137

    assert experimental_exchangeability("W", "I", False, warning=False) is None
    assert experimental_exchangeability("I", "W", False, warning=False) == 73

    assert experimental_exchangeability("N", "N", False, warning=False) == 0
    assert experimental_exchangeability("I", "I", False, warning=False) == 0
    assert experimental_exchangeability("L", "L", False, warning=False) == 0
    assert experimental_exchangeability("M", "M", False, warning=False) == 0
    assert experimental_exchangeability("W", "W", False, warning=False) == 0
    assert experimental_exchangeability("H", "H", False, warning=False) == 0
