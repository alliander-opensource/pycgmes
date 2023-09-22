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
class CogenerationPlant(PowerSystemResource, ModuleType):
    """
    A set of thermal generating units for the production of electrical energy and process steam (usually from the output
      of the steam turbines). The steam sendout is typically used for industrial purposes or for municipal heating
      and cooling.

    ThermalGeneratingUnits: A thermal generating unit may be a member of a cogeneration plant.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return CogenerationPlant(*args, **kwargs)

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
# "import CogenerationPlant"
# work as well as
# "from CogenerationPlant import CogenerationPlant".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = CogenerationPlant
