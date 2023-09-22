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

from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass(config=DataclassConfig)
class WindPlantDynamics(DynamicsFunctionBlock, ModuleType):
    """
    Parent class supporting relationships to wind turbines type 3 and type 4 and wind plant IEC and user-defined wind
      plants including their control models.

    RemoteInputSignal: The remote signal with which this power plant is associated.
    WindTurbineType3or4Dynamics: The wind turbine type 3 or type 4 associated with this wind plant.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return WindPlantDynamics(*args, **kwargs)

    RemoteInputSignal: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType3or4Dynamics : list = Field(default_factory=list, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import WindPlantDynamics"
# work as well as
# "from WindPlantDynamics import WindPlantDynamics".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = WindPlantDynamics
