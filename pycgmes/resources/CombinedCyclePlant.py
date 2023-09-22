"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .PowerSystemResource import PowerSystemResource


@dataclass(config=DataclassConfig)
class CombinedCyclePlant(PowerSystemResource, ModuleType):
    """
    A set of combustion turbines and steam turbines where the exhaust heat from the combustion turbines is recovered to
      make steam for the steam turbines, resulting in greater overall plant efficiency.

    ThermalGeneratingUnits: A thermal generating unit may be a member of a combined cycle plant.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return CombinedCyclePlant(*args, **kwargs)

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # ThermalGeneratingUnits : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

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
# "import CombinedCyclePlant"
# work as well as
# "from CombinedCyclePlant import CombinedCyclePlant".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = CombinedCyclePlant
