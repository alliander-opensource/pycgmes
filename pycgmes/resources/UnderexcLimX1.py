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

from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics


@dataclass(config=DataclassConfig)
class UnderexcLimX1(UnderexcitationLimiterDynamics, ModuleType):
    """
    Allis-Chalmers minimum excitation limiter.

    kf2: Differential gain (KF2).
    tf2: Differential time constant (TF2) (>= 0).
    km: Minimum excitation limit gain (KM).
    tm: Minimum excitation limit time constant (TM) (>= 0).
    melmax: Minimum excitation limit value (MELMAX).
    k: Minimum excitation limit slope (K) (> 0).
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return UnderexcLimX1(*args, **kwargs)

    kf2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tf2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    km: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tm: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    melmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k: float = Field(
        default=0.0,
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
# "import UnderexcLimX1"
# work as well as
# "from UnderexcLimX1 import UnderexcLimX1".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = UnderexcLimX1
