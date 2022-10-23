import logging
from functools import wraps

CORRESPONDENCE_TABLE: dict[str, str] = {
    "CYS": "C",
    "ASP": "D",
    "SER": "S",
    "GLN": "Q",
    "LYS": "K",
    "ILE": "I",
    "PRO": "P",
    "THR": "T",
    "PHE": "F",
    "ASN": "N",
    "GLY": "G",
    "HIS": "H",
    "LEU": "L",
    "ARG": "R",
    "TRP": "W",
    "ALA": "A",
    "VAL": "V",
    "GLU": "E",
    "TYR": "Y",
    "MET": "M",
}


def formatting(amino_acid: str) -> str:
    if len(amino_acid) == 3:
        amino_acid_formatted = CORRESPONDENCE_TABLE[amino_acid.upper()]
    elif len(amino_acid) == 1:
        amino_acid_formatted = amino_acid
    else:
        logging.error(f"Fatal error, {amino_acid} is not of length 1 or 3.")
        exit(1)

    return amino_acid_formatted  # noqa; warning doesn't need to be since there is an exit


def handling_3_letter_code(f):
    @wraps(f)
    def wrapper(amino_acid_1: str, amino_acid_2: str, *args, **kwargs) -> any:
        """
        transforms amino_acid_1 and amino_acid_2 in one letter code if they're in 3 letter code format
        then calls the decorated function

        return type is f return type
        """
        amino_acid_1_formatted: str = formatting(amino_acid_1)
        amino_acid_2_formatted: str = formatting(amino_acid_2)
        return f(amino_acid_1_formatted, amino_acid_2_formatted, *args, **kwargs)
    return wrapper
