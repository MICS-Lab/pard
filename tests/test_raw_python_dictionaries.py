from pard.raw_python_dictionaries import make_sneath_dict, make_grantham_dict

def test_length_dict() -> None:
    sneath_dict: dict[tuple[str, str], int] = make_sneath_dict()
    grantham_dict: dict[tuple[str, str], int] = make_grantham_dict()

    assert(len(sneath_dict) == 400)
    assert(len(grantham_dict) == 400)
