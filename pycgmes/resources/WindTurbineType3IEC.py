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

from .WindTurbineType3or4IEC import WindTurbineType3or4IEC


@dataclass(config=DataclassConfig)
class WindTurbineType3IEC(WindTurbineType3or4IEC, ModuleType):
    """
    Parent class supporting relationships to IEC wind turbines type 3 including their control models.

    WindAeroOneDimIEC: Wind aerodynamic model associated with this wind generator type 3 model.
    WindAeroTwoDimIEC: Wind aerodynamic model associated with this wind turbine type 3 model.
    WindContPitchAngleIEC: Wind control pitch angle model associated with this wind turbine type 3.
    WindContPType3IEC: Wind control P type 3 model associated with this wind turbine type 3 model.
    WindGenType3IEC: Wind generator type 3 model associated with this wind turbine type 3 model.
    WindMechIEC: Wind mechanical model associated with this wind turbine type 3 model.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return WindTurbineType3IEC(*args, **kwargs)

    WindAeroOneDimIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindAeroTwoDimIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindContPitchAngleIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindContPType3IEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindGenType3IEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindMechIEC: Optional[str] = Field(
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
# "import WindTurbineType3IEC"
# work as well as
# "from WindTurbineType3IEC import WindTurbineType3IEC".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = WindTurbineType3IEC
