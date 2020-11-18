import toml
from pyprojroot import here

from protocol_lib import __version__


def test_version() -> None:
    pyproject = toml.load(here("pyproject.toml"))
    pyproject_version = pyproject["tool"]["poetry"]["version"]

    assert __version__ == pyproject_version
