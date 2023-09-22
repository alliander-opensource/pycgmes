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

from .WindPlantDynamics import WindPlantDynamics


@dataclass(config=DataclassConfig)
class WindPlantIEC(WindPlantDynamics, ModuleType):
    """
    Simplified IEC type plant level model.  Reference: IEC 61400-27-1:2015, Annex D.

    WindPlantFreqPcontrolIEC: Wind plant frequency and active power control model associated with this wind plant.
    WindPlantReactiveControlIEC: Wind plant model with which this wind reactive control is associated.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return WindPlantIEC(*args, **kwargs)

    WindPlantFreqPcontrolIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindPlantReactiveControlIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

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
# "import WindPlantIEC"
# work as well as
# "from WindPlantIEC import WindPlantIEC".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = WindPlantIEC
