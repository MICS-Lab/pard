from pard._handling_3_letter_code_decorator import handling_3_letter_code

@handling_3_letter_code
def p_distance(amino_acid_1: str, amino_acid_2: str) -> float:
    """
    The pairwise amino acid p-distance is a measurement that solely considers the number of differences between amino
    acids in a sequence, without taking into account their properties or relationships. In this approach, all
    nonidentical amino acids are considered equal.

    :param amino_acid_1: 1 letter code of the first amino acid
    :param amino_acid_2: 1 letter code of the third amino acid

    :return: An integer representing the p-distance (pairwise amino acid distance) between amino_acid_1 and amino_acid_2
    """
    if amino_acid_1 == amino_acid_2:
        return 0
    else:
        return 1
