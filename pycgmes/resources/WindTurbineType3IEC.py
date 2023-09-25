"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .WindTurbineType3or4IEC import WindTurbineType3or4IEC


@dataclass(config=DataclassConfig)
class WindTurbineType3IEC(WindTurbineType3or4IEC):
    """
    Parent class supporting relationships to IEC wind turbines type 3 including their control models.

    WindAeroOneDimIEC: Wind aerodynamic model associated with this wind generator type 3 model.
    WindAeroTwoDimIEC: Wind aerodynamic model associated with this wind turbine type 3 model.
    WindContPitchAngleIEC: Wind control pitch angle model associated with this wind turbine type 3.
    WindContPType3IEC: Wind control P type 3 model associated with this wind turbine type 3 model.
    WindGenType3IEC: Wind generator type 3 model associated with this wind turbine type 3 model.
    WindMechIEC: Wind mechanical model associated with this wind turbine type 3 model.
    """

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
