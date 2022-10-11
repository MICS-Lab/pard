from enum import Enum
import logging

import pard.raw_python_dictionaries
from pard.handling_3_letter_code_decorator import handling_3_letter_code


class MatrixType(Enum):
    ALL_RESIDUES = 1
    HELIX = 2
    SHEET = 3
    EXPOSED = 4
    BURIED = 5
    TURN = 6
    COIL = 7
    BURIED_HELIX = 8
    BURIED_SHEET = 9
    BURIED_TURN = 10
    BURIED_COIL = 11
    EXPOSED_TURN = 12
    EXPOSED_COIL = 13


@handling_3_letter_code
def koshi_goldstein(
        amino_acid_1: str,
        amino_acid_2: str,
        matrix_type: MatrixType,
        symmetric: bool,
        warning: bool = True,
) -> float:
    """
    :param amino_acid_1: 1 letter code of the first amino acid
    :param amino_acid_2: 1 letter code of the third amino acid
    :param matrix_type: which optimal Koshi-Goldstein substitution matrix is desired
    :param symmetric: whether the symmetric version of the matrix is wanted or not (i.e. exchanges of known* or
                      unknown direction)
                      * amino_acid_1 -> amino_acid_2
    :param warning: Set warning to False to stop seeing the warning

    :return: An integer / float / None representing the experimental exchangeability distance between amino_acid_1 and
             amino_acid_2 (x1000)
    """
    if warning:
        logging.warning(" Friendly reminder that the koshi_goldstein score is not a distance. Rather, it is the "
                        "likelihood of a mutation from amino_acid_1 to amino_acid_2. Meaning, high koshi_goldstein "
                        "score is likely to mean that the amino acids are similar, although this statement certainly "
                        "is debatable.\n"
                        "To remove this warning, call the function koshi_goldstein with the optional argument "
                        "'warning=False'.")
    if symmetric:
        return pard.raw_python_dictionaries.SYMMETRIC_KOSHI_GOLDSTEIN_DICT[(amino_acid_1, amino_acid_2)]
    else:
        return pard.raw_python_dictionaries.ASYMMETRIC_KOSHI_GOLDSTEIN_DICT[(amino_acid_1, amino_acid_2)]
