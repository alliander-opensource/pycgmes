"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindContPitchAngleIEC(IdentifiedObject, ModuleType):
    """
    Pitch angle control model. Reference: IEC 61400-27-1:2015, 5.6.5.2.

    dthetamax: Maximum pitch positive ramp rate (dthetamax) (> WindContPitchAngleIEC.dthetamin). It is a type-dependent
      parameter. Unit = degrees / s.
    dthetamin: Maximum pitch negative ramp rate (dthetamin) (< WindContPitchAngleIEC.dthetamax). It is a type-dependent
      parameter. Unit = degrees / s.
    kic: Power PI controller integration gain (KIc). It is a type-dependent parameter.
    kiomega: Speed PI controller integration gain (KIomega). It is a type-dependent parameter.
    kpc: Power PI controller proportional gain (KPc). It is a type-dependent parameter.
    kpomega: Speed PI controller proportional gain (KPomega). It is a type-dependent parameter.
    kpx: Pitch cross coupling gain (KPX). It is a type-dependent parameter.
    thetamax: Maximum pitch angle (thetamax) (> WindContPitchAngleIEC.thetamin). It is a type-dependent parameter.
    thetamin: Minimum pitch angle (thetamin) (< WindContPitchAngleIEC.thetamax). It is a type-dependent parameter.
    ttheta: Pitch time constant (ttheta) (>= 0). It is a type-dependent parameter.
    WindTurbineType3IEC: Wind turbine type 3 model with which this pitch control model is associated.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return WindContPitchAngleIEC(*args, **kwargs)

    dthetamax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dthetamin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kic: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kiomega: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kpc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kpomega: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kpx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    thetamax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    thetamin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ttheta: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType3IEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

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
# "import WindContPitchAngleIEC"
# work as well as
# "from WindContPitchAngleIEC import WindContPitchAngleIEC".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = WindContPitchAngleIEC
