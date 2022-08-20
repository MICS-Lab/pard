from pard.raw_python_dictionaries import make_grantham_dict

GRANTHAM_DICT: dict[tuple[str, str], int] = make_grantham_dict()

def grantham(amino_acid_1: str, amino_acid_2: str) -> int:
    """
    :param amino_acid_1: 1 letter code of the first amino acid
    :param amino_acid_2: 1 letter code of the third amino acid
    :return: An integer representing the Grantham distance between aa_1 and amino_acid_2
    """
    return GRANTHAM_DICT[(amino_acid_1, amino_acid_2)]
