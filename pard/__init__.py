import importlib.metadata

__version__ = importlib.metadata.version("pard")

from . import sneath, miyata, epstein, grantham
