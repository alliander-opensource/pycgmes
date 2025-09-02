# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

import importlib
from collections.abc import Iterator
from enum import EnumType
from pathlib import Path

import pytest

from pycgmes.utils.datatypes import CIMDatatype, Primitive


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
        cls = getattr(mod, resource)
        if type(cls) not in (Primitive, CIMDatatype, EnumType):
            profiles = cls().possible_profiles
            assert profiles
