import pard.raw_python_dictionaries

def miyata(amino_acid_1: str, amino_acid_2: str) -> float:
    """
    :param amino_acid_1: 1 letter code of the first amino acid
    :param amino_acid_2: 1 letter code of the third amino acid

    :return: An integer representing the Miyata distance between aa_1 and amino_acid_2
    """
    return pard.raw_python_dictionaries.MIYATA_DICT[(amino_acid_1, amino_acid_2)]
