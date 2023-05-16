## PARD (Physicochemical Amino acid Replacement Distances)
[![DOI](https://zenodo.org/badge/526882024.svg)](https://zenodo.org/badge/latestdoi/526882024)
![Coverage](
readme_resources/coverage.svg
)
[![Downloads](https://pepy.tech/badge/pard)](https://pepy.tech/project/pard)

### Overview
Amino acid replacements (also referred to as substitutions) are changes from one amino acid to a different one in a
protein - and there are different ways to assess the difference between the two amino acids that come into play in an
amino acid replacement.

One can look at one or several properties' discrepancy between two amino acids.
To list only a few: polarity
[[1]](https://www.science.org/doi/10.1126/science.185.4154.862) [[3]](https://www.nature.com/articles/215355a0) 
[[4]](https://link.springer.com/article/10.1007/BF01732340) 
[[8]](https://onlinelibrary.wiley.com/doi/10.1111/j.1399-3011.1987.tb02254.x),
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
[[5]](https://pubmed.ncbi.nlm.nih.gov/15944362/), Chou-Fasman alpha helical, beta strand and reverse turn
propensity parameters [[8]](https://onlinelibrary.wiley.com/doi/10.1111/j.1399-3011.1987.tb02254.x), etc.

`pard` is a package designed to make those **P**hysicochemical **A**mino acid **R**eplacement **D**istances calculations
straightforward with Python.

One typical use is to establish a 'distance' between a wild-type protein and its mutated version. Sometimes, rather
than a distance, a similarity is outputted (e.g. with `the Conformational similarity weight matrix`
[[7]](https://www.sciencedirect.com/science/article/abs/pii/002228369290261H) or `EMPAR` 
[[8]](https://onlinelibrary.wiley.com/doi/10.1111/j.1399-3011.1987.tb02254.x)). The higher the distance, the more
different the two amino acids are. The higher the similarity, the more similar the two amino acids are. Whenever
a distance is not outputted but rather a similarity, a warning (that the user can turn off) will be raised.


### Getting started
#### Install from PyPI (recommended)
To use `pard`, run `pip install pard` in your terminal.

#### Usage
```py
## Imports
from pard.grantham import grantham
from pard.sneath import sneath
from pard.experimental_exchangeability import experimental_exchangeability
from pard.koshi_goldstein import koshi_goldstein, MatrixType


## Basic examples
amino_acid_1: str = "W"  # Tryptophan
amino_acid_2: str = "L"  # Leucine
distance_grantham: int = grantham(amino_acid_1, amino_acid_2)
print(distance_grantham)

distance_sneath: int   = sneath(amino_acid_1, amino_acid_2)
print(distance_sneath)

distance_ee: float     = experimental_exchangeability(
    amino_acid_1, 
    amino_acid_2, 
    False, 
    warning=True
)
print(distance_ee)


## More subtle examples
# Koshi-Goldstein has several scores and can estimate the likelihood of InDels
distance_koshi_goldstein_all: float = koshi_goldstein(
    "-",
    "A",
    MatrixType.ALL_RESIDUES,
    False,
    warning=True
)
print(distance_koshi_goldstein_all)
```
or equivalently
```py
## Imports
import pard


## Basic examples
amino_acid_1: str = "W"  # Tryptophan
amino_acid_2: str = "L"  # Leucine
distance_grantham: int = pard.grantham.grantham(amino_acid_1, amino_acid_2)
print(distance_grantham)

distance_sneath: int   = pard.sneath.sneath(amino_acid_1, amino_acid_2)
print(distance_sneath)

distance_ee: float     = pard.experimental_exchangeability.experimental_exchangeability(
    amino_acid_1,
    amino_acid_2,
    False,
    warning=True
)
print(distance_ee)


## More subtle examples
# Koshi-Goldstein has several scores and can estimate the likelihood of InDels
distance_koshi_goldstein_all: float = pard.koshi_goldstein.koshi_goldstein(
    "-",
    "A",
    pard.koshi_goldstein.MatrixType.ALL_RESIDUES,
    False,
    warning=True
)
print(distance_koshi_goldstein_all)
```
will output:
```
>>> 61
>>> 30
>>> 177
>>> 1.6
```
which are the correct values 
[[1]](https://www.science.org/doi/10.1126/science.185.4154.862)
[[2]](https://www.sciencedirect.com/science/article/abs/pii/0022519366901123)
[[5]](https://pubmed.ncbi.nlm.nih.gov/15944362/)
[[6]](https://academic.oup.com/peds/article-abstract/8/7/641/1465446)
.

#### Exit codes:
```
- 1: Argument amino_acid_1 or amino_acid_2 is neither of length 1 nor length 3. See error message.
```

### About the source code
- Follows [PEP8](https://peps.python.org/pep-0008/) Style Guidelines.
- All functions are unit-tested with [pytest](https://docs.pytest.org/en/6.2.x/).
- All variables are correctly type-hinted, reviewed with [static type checker](https://mypy.readthedocs.io/en/stable/)
`mypy`.
- All functions are documented with [docstrings](https://www.python.org/dev/peps/pep-0257/).


#### Unit tests details
Coverage
```
Name                                         Stmts   Miss  Cover
----------------------------------------------------------------
pard\__init__.py                                 3      0   100%
pard\_handling_3_letter_code_decorator.py       18      2    89%
pard\_raw_python_dictionaries.py                71      0   100%
pard\empar.py                                    8      0   100%
pard\epstein.py                                  7      0   100%
pard\experimental_exchangeability.py            10      0   100%
pard\grantham.py                                 5      0   100%
pard\kolaskar.py                                 8      0   100%
pard\koshi_goldstein.py                         55      2    96%
pard\miyata.py                                   5      0   100%
pard\sneath.py                                   5      0   100%
tests\__init__.py                                0      0   100%
tests\test_empar.py                             26      0   100%
tests\test_epstein.py                           46      0   100%
tests\test_experimental_exchangeability.py      30      0   100%
tests\test_grantham.py                          25      0   100%
tests\test_kolaskar.py                          26      0   100%
tests\test_koshi_goldstein.py                  108      0   100%
tests\test_miyata.py                            25      0   100%
tests\test_pard.py                               3      0   100%
tests\test_raw_python_dictionaries.py           24      0   100%
tests\test_sneath.py                            21      0   100%
unit_tests_simple.py                             5      0   100%
----------------------------------------------------------------
TOTAL                                          534      4    99%
```

#### pytest
```
platform win32 -- Python 3.11.1, pytest-7.2.0, pluggy-1.0.0
plugins: anyio-3.6.2, mypy-0.10.3
collected 16 items

tests\test_empar.py .                                     [  6%] 
tests\test_epstein.py .                                   [ 12%] 
tests\test_experimental_exchangeability.py .              [ 18%] 
tests\test_grantham.py .                                  [ 25%]
tests\test_kolaskar.py .                                  [ 31%] 
tests\test_koshi_goldstein.py .......                     [ 75%]
tests\test_miyata.py .                                    [ 81%] 
tests\test_pard.py .                                      [ 87%] 
tests\test_raw_python_dictionaries.py .                   [ 93%] 
tests\test_sneath.py .                                    [100%] 

====================== 16 passed in 0.11s ====================== 
```

#### mypy detail
```
================================== mypy ==================================
Success: no issues found in 24 source files
```

### Useful links:
- [Corresponding GitHub repository](https://github.com/MICS-Lab/pard)
- [Corresponding PyPI page](https://pypi.org/project/pard/)


### Citation
If you use this software, please cite it as below.

- APA:

`
Lhotte, R. & Taupin, J. (2022).
Physicochemical Amino acid Replacement Distances (PARD) package (Version 0.6.0.0) [Computer software].
https://doi.org/10.5281/zenodo.7013169
`

- BibTeX:

```
@software{lhotte_pard_2022,
    author = {Lhotte, Romain and Taupin, Jean-Luc},
    doi = {10.5281/zenodo.7013169},
    month = {8},
    title = {{Physicochemical Amino acid Replacement Distances (PARD) package}},
    version = {0.6.0.0},
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
- [6] Koshi, J.M. and Goldstein, R.A., 1995. Context-dependent optimal substitution matrices. Protein Engineering,
Design and Selection, 8(7), pp.641-645.
