from pard.empar import empar


def test_empar() -> None:
    for warning in [True, False]:
        assert empar("L", "I", warning=warning) == 10
        assert empar("Leu", "Ile", warning=warning) == 10
        assert empar("leu", "ile", warning=warning) == 10
        assert empar("L", "ile", warning=warning) == 10
        assert empar("I", "L", warning=warning) == 10
        assert empar("Ile", "Leu", warning=warning) == 10
        assert empar("ILE", "LEU", warning=warning) == 10
        assert empar("ILE", "L", warning=warning) == 10

        assert empar("N", "I", warning=warning) == 5
        assert empar("I", "N", warning=warning) == 5

        assert empar("N", "L", warning=warning) == 7
        assert empar("L", "N", warning=warning) == 7

        assert empar("M", "W", warning=warning) == 10
        assert empar("W", "M", warning=warning) == 10

        assert empar("L", "W", warning=warning) == 11
        assert empar("W", "L", warning=warning) == 11

        assert empar("N", "N", warning=warning) == 16
        assert empar("I", "I", warning=warning) == 16
        assert empar("L", "L", warning=warning) == 16
        assert empar("M", "M", warning=warning) == 16
        assert empar("W", "W", warning=warning) == 16
        assert empar("H", "H", warning=warning) == 16
        assert empar("His", "His", warning=warning) == 16
