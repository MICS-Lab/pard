import pard.raw_python_dictionaries
from pard.handling_3_letter_code_decorator import handling_3_letter_code

@handling_3_letter_code
def grantham(amino_acid_1: str, amino_acid_2: str) -> int:
    """
    :param amino_acid_1: 1 letter code of the first amino acid
    :param amino_acid_2: 1 letter code of the third amino acid

    :return: An integer representing the Grantham distance between amino_acid_1 and amino_acid_2
    """
    return pard.raw_python_dictionaries.GRANTHAM_DICT[(amino_acid_1, amino_acid_2)]
