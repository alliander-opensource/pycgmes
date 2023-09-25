import importlib
from pathlib import Path
from typing import Iterator

import pytest


def get_all_resources() -> Iterator[str]:
    resource_dir = Path(__file__).parent.parent / "pycgmes" / "resources"
    resources = [str(f.stem) for f in resource_dir.glob("*.py") if f.name != "__init__.py"]
    return resources


class TestLoadAll:
    # Importing all resources to make sure there is no syntax error.

    @pytest.mark.parametrize("resource", get_all_resources())
    def test_importing(self, resource):
        mod = importlib.import_module(f".{resource}", package="pycgmes.resources")
        # Calling possible profiles to have full coverage.
        getattr(mod, resource)().possible_profiles
