"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class FossilFuel(IdentifiedObject, ModuleType):
    """
    The fossil fuel consumed by the non-nuclear thermal generating unit.   For example, coal, oil, gas, etc.   These are
      the specific fuels that the generating unit can consume.

    fossilFuelType: The type of fossil fuel, such as coal, oil, or gas.
    ThermalGeneratingUnit: A thermal generating unit may have one or more fossil fuels.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return FossilFuel(*args, **kwargs)

    fossilFuelType: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    ThermalGeneratingUnit: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import FossilFuel"
# work as well as
# "from FossilFuel import FossilFuel".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = FossilFuel
