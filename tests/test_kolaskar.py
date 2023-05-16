from pard.kolaskar import kolaskar


def test_kolaskar() -> None:
    for warning in [True, False]:
        assert kolaskar("L", "I", warning=warning) == 0
        assert kolaskar("Leu", "Ile", warning=warning) == 0
        assert kolaskar("leu", "ile", warning=warning) == 0
        assert kolaskar("L", "ile", warning=warning) == 0
        assert kolaskar("I", "L", warning=warning) == 0
        assert kolaskar("Ile", "Leu", warning=warning) == 0
        assert kolaskar("ILE", "LEU", warning=warning) == 0
        assert kolaskar("ILE", "L", warning=warning) == 0

        assert kolaskar("N", "I", warning=warning) == 0
        assert kolaskar("I", "N", warning=warning) == 0

        assert kolaskar("N", "L", warning=warning) == 0
        assert kolaskar("L", "N", warning=warning) == 0

        assert kolaskar("M", "W", warning=warning) == 6.6
        assert kolaskar("W", "M", warning=warning) == 6.6

        assert kolaskar("L", "W", warning=warning) == 5
        assert kolaskar("W", "L", warning=warning) == 5

        assert kolaskar("N", "N", warning=warning) == 10
        assert kolaskar("I", "I", warning=warning) == 10
        assert kolaskar("L", "L", warning=warning) == 10
        assert kolaskar("M", "M", warning=warning) == 10
        assert kolaskar("W", "W", warning=warning) == 10
        assert kolaskar("H", "H", warning=warning) == 10
        assert kolaskar("His", "His", warning=warning) == 10
