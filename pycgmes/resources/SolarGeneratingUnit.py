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

from .GeneratingUnit import GeneratingUnit


@dataclass(config=DataclassConfig)
class SolarGeneratingUnit(GeneratingUnit, ModuleType):
    """
    A solar thermal generating unit, connected to the grid by means of a rotating machine.  This class does not
      represent photovoltaic (PV) generation.

    SolarPowerPlant: A solar power plant may have solar generating units.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return SolarGeneratingUnit(*args, **kwargs)

    SolarPowerPlant: Optional[str] = Field(
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
            Profile.SSH,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import SolarGeneratingUnit"
# work as well as
# "from SolarGeneratingUnit import SolarGeneratingUnit".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = SolarGeneratingUnit
