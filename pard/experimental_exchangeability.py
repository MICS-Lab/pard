import logging

import pard.raw_python_dictionaries
from pard.handling_3_letter_code_decorator import handling_3_letter_code

@handling_3_letter_code
def experimental_exchangeability(
        amino_acid_1: str,
        amino_acid_2: str,
        symmetric: bool,
        warning: bool = True,
) -> float | int | None:
    """
    :param amino_acid_1: 1 letter code of the first amino acid
    :param amino_acid_2: 1 letter code of the third amino acid
    :param symmetric: whether the symmetric version of the matrix is wanted or not (i.e. exchanges of known or
                      unknown direction)
    :param warning: Set warning to False to stop seeing the warning

    :return: An integer / float / None representing the experimental exchangeability distance between amino_acid_1 and
             amino_acid_2 (x1000)
    """
    if warning:
        logging.warning(" Friendly reminder that exchangeability is not a distance. Rather, it is the mean activity of"
                        " variants with an exchange from amino acid amino_acid_1 to amino_acid_2. Meaning, high "
                        "exchangeability is likely to mean that the amino acids are similar, although this statement is"
                        " debatable. \n"
                        "To remove this warning, call the function experimental_exchangeability with the optional"
                        "argument 'warning=False'.")
    if symmetric:
        return pard.raw_python_dictionaries.SYMMETRIC_EXPERIMENTAL_EXCHANGEABILITY_DICT[(amino_acid_1, amino_acid_2)]
    else:
        return pard.raw_python_dictionaries.ASYMMETRIC_EXPERIMENTAL_EXCHANGEABILITY_DICT[(amino_acid_1, amino_acid_2)]
