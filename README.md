## PARD (Physicochemical Amino acid Replacement Distances)


### Overview
Amino acid replacements (also referred to as substitutions) are changes from one amino acid to a different one in a
protein - and there are different ways to assess the difference between the two amino acids that come into play in an
amino acid replacement.
One can look at one or several properties' discrepancy between two amino acids. To list only a few: polarity [1][3][4],
molecular volume / relative sizes of amino-acid side chains [1][3][4], mean number of lone pair electrons on the 
side-chain [2], maximum moment of inertia for rotation at the α―β bond [2] or at the β―γ bond [2] or at the γ―δ
bond [2], presence of a pyrrolidine ring (proline (P)) [2], experimental protein activity and stability after 
exchanging one amino acid into another [5], etc.).


### Getting started
`pard` is a package designed to make **P**hysicochemical **A**mino acid **R**eplacement **D**istances calculations
straightforward.

#### Install from PyPI (recommended)
To use `pard`, run `pip install pard` in your terminal.

#### Usage


#### Unit tests
```
Name                              Stmts   Miss  Cover

-----------------------------------------------------
pard\__init__.py                      2      0   100%
pard\grantham.py                      4      0   100%
pard\raw_python_dictionaries.py      18     10    44%
tests\__init__.py                     0      0   100%
tests\test_grantham.py               15      0   100%
tests\test_pard.py                    3      0   100%
-----------------------------------------------------
TOTAL                                42     10    76%
```


### About the source code
- Follows [PEP8](https://peps.python.org/pep-0008/) Style Guidelines.
- All variables are correctly type-hinted, reviewed with [static type checker](https://mypy.readthedocs.io/en/stable/)
`mypy`.


### Useful links:
- [Corresponding GitHub repository](https://github.com/MICS-Lab/pard)
- [Corresponding PyPI page](https://pypi.org/project/pard/)


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
