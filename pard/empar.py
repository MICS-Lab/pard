import logging

import pard._raw_python_dictionaries
from pard._handling_3_letter_code_decorator import handling_3_letter_code


@handling_3_letter_code
def empar(
    amino_acid_1: str,
    amino_acid_2: str,
    warning: bool = True,
) -> float | int | None:
    """
    :param amino_acid_1: 1 letter code of the first amino acid
    :param amino_acid_2: 1 letter code of the third amino acid
    :param warning: Set warning to False to stop seeing the warning

    :return: A float representing the EMPAR (Exchange Matrix derived from PARameters) similarity between
             amino_acid_1 and amino_acid_2
    """
    if warning:
        logging.warning(
            " Friendly reminder that the EMPAR (Exchange Matrix derived from PARameters) score is not a 'distance'"
            " but rather a 'similarity'. This means that the higher the value, the more similar the amino acids"
            " are. To remove this warning, call the function kolaskar with the optional argument 'warning=False'."
        )
    return pard._raw_python_dictionaries.EMPAR_DICT[(amino_acid_1, amino_acid_2)]
