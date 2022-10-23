import pytest

retcode: int | pytest.ExitCode = pytest.main([])

if retcode == pytest.ExitCode.OK:
    print("\n--- \nAll good.\n--- \n")
