from pard.raw_python_dictionaries import (
    make_sneath_dict,
    make_miyata_dict,
    make_symmetric_epstein_dict,
    make_asymmetric_epstein_dict,
    make_grantham_dict,
)

def test_length_dict() -> None:
    sneath_dict: dict[tuple[str, str], int]               = make_sneath_dict()
    miyata_dict: dict[tuple[str, str], float]             = make_miyata_dict()
    symmetric_epstein_dict: dict[tuple[str, str], float]  = make_symmetric_epstein_dict()
    asymmetric_epstein_dict: dict[tuple[str, str], float] = make_asymmetric_epstein_dict()
    grantham_dict: dict[tuple[str, str], int]             = make_grantham_dict()

    assert(len(sneath_dict) == 400)
    assert(len(miyata_dict) == 400)
    assert(len(symmetric_epstein_dict) == 400)
    assert(len(asymmetric_epstein_dict) == 400)
    assert(len(grantham_dict) == 400)
