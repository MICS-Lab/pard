## PARD (Physicochemical Amino acid Replacement Distances)
[![DOI](https://zenodo.org/badge/526882024.svg)](https://zenodo.org/badge/latestdoi/526882024)
![Coverage](
https://raw.githubusercontent.com/MICS-Lab/pard/a0633c0b5e95bff565c6b9f92811b8b7bc0c8a6b/readme_resources/coverage.svg
)

### Overview
Amino acid replacements (also referred to as substitutions) are changes from one amino acid to a different one in a
protein - and there are different ways to assess the difference between the two amino acids that come into play in an
amino acid replacement.

One can look at one or several properties' discrepancy between two amino acids.
To list only a few: polarity
[[1]](https://www.science.org/doi/10.1126/science.185.4154.862) [[3]](https://www.nature.com/articles/215355a0) 
[[4]](https://link.springer.com/article/10.1007/BF01732340),
molecular volume / relative sizes of amino-acid side chains 
[[1]](https://www.science.org/doi/10.1126/science.185.4154.862) [[3]](https://www.nature.com/articles/215355a0)
[[4]](https://link.springer.com/article/10.1007/BF01732340), 
mean number of lone pair electrons on the side-chain
[[2]](https://www.sciencedirect.com/science/article/abs/pii/0022519366901123),
maximum moment of inertia for rotation at the α―β bond
[[2]](https://www.sciencedirect.com/science/article/abs/pii/0022519366901123)
or at the β―γ bond [[2]](https://www.sciencedirect.com/science/article/abs/pii/0022519366901123)
or at the γ―δ bond [[2]](https://www.sciencedirect.com/science/article/abs/pii/0022519366901123), 
presence of a pyrrolidine ring (proline (P))
[[2]](https://www.sciencedirect.com/science/article/abs/pii/0022519366901123), 
experimental protein activity and stability after exchanging one amino acid into another
[[5]](https://pubmed.ncbi.nlm.nih.gov/15944362/),
etc.

`pard` is a package designed to make those **P**hysicochemical **A**mino acid **R**eplacement **D**istances calculations
straightforward with Python.

One typical use is to establish a 'distance' between a wild-type protein and its mutated version.


### Getting started
#### Install from PyPI (recommended)
To use `pard`, run `pip install pard` in your terminal.

#### Usage
```py
import pard

amino_acid_1: str = "W"  # Tryptophan
amino_acid_2: str = "L"  # Leucine
distance_grantham: int = pard.grantham.grantham(amino_acid_1, amino_acid_2)
distance_sneath: int   = pard.sneath.sneath(amino_acid_1, amino_acid_2)
distance_ee: float     = pard.experimental_exchangeability.experimental_exchangeability(
    amino_acid_1, 
    amino_acid_2, 
    False, 
    warning=False
)

print(distance_grantham)
print(distance_sneath)
print(distance_ee)
```
or equivalently
```py
from pard.grantham import grantham
from pard.sneath import sneath
from pard.experimental_exchangeability import experimental_exchangeability

amino_acid_1: str = "W"  # Tryptophan
amino_acid_2: str = "L"  # Leucine
distance_grantham: int = grantham(amino_acid_1, amino_acid_2)
distance_sneath: int   = sneath(amino_acid_1, amino_acid_2)
distance_ee: float     = experimental_exchangeability(amino_acid_1, amino_acid_2, False, warning=False)

print(distance_grantham)
print(distance_sneath)
print(distance_ee)
```
will output:
```
>>> 61
>>> 30
>>> 177
```
which are the correct values 
[[1]](https://www.science.org/doi/10.1126/science.185.4154.862)
[[2]](https://www.sciencedirect.com/science/article/abs/pii/0022519366901123)
[[5]](https://pubmed.ncbi.nlm.nih.gov/15944362/)
.

#### Exit codes:
```
- 1: Argument amino_acid_1 or amino_acid_2 is neither of length 1 nor length 3. See error message.
```

#### Unit tests
```
Name                                         Stmts   Miss  Cover
----------------------------------------------------------------
pard\__init__.py                                 3      0   100%
pard\epstein.py                                  5      0   100%
pard\experimental_exchangeability.py             8      1    88%
pard\grantham.py                                 3      0   100%
pard\miyata.py                                   3      0   100%
pard\raw_python_dictionaries.py                 35      0   100%
pard\sneath.py                                   3      0   100%
tests\__init__.py                                0      0   100%
tests\test_epstein.py                           34      0   100%
tests\test_experimental_exchangeability.py      22      0   100%
tests\test_grantham.py                          18      0   100%
tests\test_miyata.py                            18      0   100%
tests\test_pard.py                               3      0   100%
tests\test_raw_python_dictionaries.py           12      0   100%
tests\test_sneath.py                            18      0   100%
----------------------------------------------------------------
TOTAL                                          185      1    99%
```


### About the source code
- Follows [PEP8](https://peps.python.org/pep-0008/) Style Guidelines.
- All variables are correctly type-hinted, reviewed with [static type checker](https://mypy.readthedocs.io/en/stable/)
`mypy`.


### Useful links:
- [Corresponding GitHub repository](https://github.com/MICS-Lab/pard)
- [Corresponding PyPI page](https://pypi.org/project/pard/)


### Citation
If you use this software, please cite it as below.

- APA:

`
Lhotte, R. & Taupin, J. (2022).
Physicochemical Amino acid Replacement Distances (PARD) package (Version 0.1.7.1) [Computer software].
https://doi.org/10.5281/zenodo.7013169
`

- BibTeX:

```
@software{lhotte_pard_2022,
author = {Lhotte, Romain and Taupin, Jean-Luc},
doi = {10.5281/zenodo.7013169},
month = {8},
title = {{Physicochemical Amino acid Replacement Distances (PARD) package}},
version = {0.1.7.1},
year = {2022}
}
```


### References
- [1] Grantham, R., 1974. Amino acid difference formula to help explain protein evolution. science, 185(4154), 
pp.862-864.
- [2] Sneath, P.H.A., 1966. Relations between chemical structure and biological activity in peptides. Journal of
theoretical biology, 12(2), pp.157-195.
- [3] Epstein, C.J., 1967. Non-randomness of ammo-acid changes in the evolution of homologous proteins. Nature,
215(5099), pp.355-359.
- [4] Miyata, T., Miyazawa, S. and Yasunaga, T., 1979. Two types of amino acid substitutions in protein evolution. 
Journal of molecular evolution, 12(3), pp.219-236.
- [5] Yampolsky, L.Y. and Stoltzfus, A., 2005. The exchangeability of amino acids in proteins. Genetics, 170(4), 
pp.1459-1472.
