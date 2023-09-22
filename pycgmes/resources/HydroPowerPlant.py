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

from .PowerSystemResource import PowerSystemResource


@dataclass(config=DataclassConfig)
class HydroPowerPlant(PowerSystemResource, ModuleType):
    """
    A hydro power station which can generate or pump. When generating, the generator turbines receive water from an
      upper reservoir. When pumping, the pumps receive their water from a lower reservoir.

    HydroGeneratingUnits: The hydro generating unit belongs to a hydro power plant.
    hydroPlantStorageType: The type of hydro power plant water storage.
    HydroPumps: The hydro pump may be a member of a pumped storage plant or a pump for distributing water.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return HydroPowerPlant(*args, **kwargs)

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # HydroGeneratingUnits : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    hydroPlantStorageType: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # HydroPumps : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

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
# "import HydroPowerPlant"
# work as well as
# "from HydroPowerPlant import HydroPowerPlant".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = HydroPowerPlant
