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
class ThermalGeneratingUnit(GeneratingUnit, ModuleType):
    """
    A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.

    CAESPlant: A thermal generating unit may be a member of a compressed air energy storage plant.
    CogenerationPlant: A thermal generating unit may be a member of a cogeneration plant.
    CombinedCyclePlant: A thermal generating unit may be a member of a combined cycle plant.
    FossilFuels: A thermal generating unit may have one or more fossil fuels.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ThermalGeneratingUnit(*args, **kwargs)

    CAESPlant: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    CogenerationPlant: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    CombinedCyclePlant: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # FossilFuels : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

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
# "import ThermalGeneratingUnit"
# work as well as
# "from ThermalGeneratingUnit import ThermalGeneratingUnit".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ThermalGeneratingUnit
