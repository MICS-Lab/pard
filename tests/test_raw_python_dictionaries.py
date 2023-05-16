from pard._raw_python_dictionaries import (  # noqa: internal use
    make_sneath_dict,
    make_miyata_dict,
    make_symmetric_epstein_dict,
    make_asymmetric_epstein_dict,
    make_kolaskar_dict,
    make_empar_dict,
    make_symmetric_experimental_exchangeability_dict,
    make_asymmetric_experimental_exchangeability_dict,
    make_grantham_dict,
    make_symmetric_koshi_golstein_dicts,
    make_asymmetric_koshi_golstein_dicts
)

def test_length_dict() -> None:
    sneath_dict: dict[tuple[str, str], int]
    miyata_dict: dict[tuple[str, str], float]
    symmetric_epstein_dict: dict[tuple[str, str], float]
    asymmetric_epstein_dict: dict[tuple[str, str], float]
    kolaskar_dict: dict[tuple[str, str], float]
    empar_dict: dict[tuple[str, str], int]
    symmetric_experimental_exchangeability_dict: dict[tuple[str, str], float]
    asymmetric_experimental_exchangeability_dict: dict[tuple[str, str], int | None]
    grantham_dict: dict[tuple[str, str], int]

    ## Getting dicts
    # Sneath dict
    sneath_dict                                  = make_sneath_dict()

    # Miyata dict
    miyata_dict                                  = make_miyata_dict()

    # Epstein dicts
    symmetric_epstein_dict                       = make_symmetric_epstein_dict()
    asymmetric_epstein_dict                      = make_asymmetric_epstein_dict()

    # Kolaskar dict
    kolaskar_dict                                = make_kolaskar_dict()

    # EMPAR dict
    empar_dict                                   = make_empar_dict()

    # Experimental exchangeability dicts
    symmetric_experimental_exchangeability_dict  = make_symmetric_experimental_exchangeability_dict()
    asymmetric_experimental_exchangeability_dict = make_asymmetric_experimental_exchangeability_dict()

    # Grantham dict
    grantham_dict                                = make_grantham_dict()

    # Koshi-Goldstein dicts
    (
        symmetric_koshi_goldstein_all_residues_dict,
        symmetric_koshi_goldstein_exposed_residues_dict,
        symmetric_koshi_goldstein_buried_residues_dict,
        symmetric_koshi_goldstein_coil_residues_dict,
        symmetric_koshi_goldstein_turn_residues_dict,
        symmetric_koshi_goldstein_helix_residues_dict,
        symmetric_koshi_goldstein_sheet_residues_dict,
    ) = make_symmetric_koshi_golstein_dicts()
    (
        asymmetric_koshi_goldstein_all_residues_dict,
        asymmetric_koshi_goldstein_exposed_residues_dict,
        asymmetric_koshi_goldstein_buried_residues_dict,
        asymmetric_koshi_goldstein_coil_residues_dict,
        asymmetric_koshi_goldstein_turn_residues_dict,
        asymmetric_koshi_goldstein_helix_residues_dict,
        asymmetric_koshi_goldstein_sheet_residues_dict,
    ) = make_asymmetric_koshi_golstein_dicts()

    ## Asserting length of dicts
    ## 20x20 matrices
    assert(len(sneath_dict) == 400)
    assert(len(miyata_dict) == 400)
    assert(len(symmetric_epstein_dict) == 400)
    assert(len(asymmetric_epstein_dict) == 400)
    assert(len(kolaskar_dict) == 400)
    assert(len(empar_dict) == 400)
    assert(len(symmetric_experimental_exchangeability_dict) == 400)
    assert(len(asymmetric_experimental_exchangeability_dict) == 400)
    assert(len(grantham_dict) == 400)

    ## 21x21 matrices
    # Koshi-Goldstein matrices
    for koshi_goldstein_dict in (
        symmetric_koshi_goldstein_all_residues_dict,
        symmetric_koshi_goldstein_exposed_residues_dict,
        symmetric_koshi_goldstein_buried_residues_dict,
        symmetric_koshi_goldstein_coil_residues_dict,
        symmetric_koshi_goldstein_turn_residues_dict,
        symmetric_koshi_goldstein_helix_residues_dict,
        symmetric_koshi_goldstein_sheet_residues_dict,
        asymmetric_koshi_goldstein_all_residues_dict,
        asymmetric_koshi_goldstein_exposed_residues_dict,
        asymmetric_koshi_goldstein_buried_residues_dict,
        asymmetric_koshi_goldstein_coil_residues_dict,
        asymmetric_koshi_goldstein_turn_residues_dict,
        asymmetric_koshi_goldstein_helix_residues_dict,
        asymmetric_koshi_goldstein_sheet_residues_dict,
    ):
        assert(len(koshi_goldstein_dict) == 441)
