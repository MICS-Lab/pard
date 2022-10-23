import pytest

retcode: int | pytest.ExitCode = pytest.main(["--mypy"])

if retcode == pytest.ExitCode.OK:
    print("\n--- \nAll good.\n--- \n")
