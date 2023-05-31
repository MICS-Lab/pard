import importlib.metadata

__version__: str = importlib.metadata.version("pard")

from . import (
    sneath,
    miyata,
    epstein,
    experimental_exchangeability,
    grantham,
    koshi_goldstein,
    kolaskar,
    empar,
    pairwise_distance
)
