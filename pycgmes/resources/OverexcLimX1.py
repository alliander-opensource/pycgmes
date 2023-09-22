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

from .OverexcitationLimiterDynamics import OverexcitationLimiterDynamics


@dataclass(config=DataclassConfig)
class OverexcLimX1(OverexcitationLimiterDynamics, ModuleType):
    """
    Field voltage over excitation limiter.

    efdrated: Rated field voltage (EFDRATED).  Typical value = 1,05.
    efd1: Low voltage point on the inverse time characteristic (EFD1).  Typical value = 1,1.
    t1: Time to trip the exciter at the low voltage point on the inverse time characteristic (TIME1) (>= 0).  Typical
      value = 120.
    efd2: Mid voltage point on the inverse time characteristic (EFD2).  Typical value = 1,2.
    t2: Time to trip the exciter at the mid voltage point on the inverse time characteristic (TIME2) (>= 0).  Typical
      value = 40.
    efd3: High voltage point on the inverse time characteristic (EFD3).  Typical value = 1,5.
    t3: Time to trip the exciter at the high voltage point on the inverse time characteristic (TIME3) (>= 0).  Typical
      value = 15.
    efddes: Desired field voltage (EFDDES).  Typical value = 0,9.
    kmx: Gain (KMX).  Typical value = 0,01.
    vlow: Low voltage limit (VLOW) (> 0).
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return OverexcLimX1(*args, **kwargs)

    efdrated: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efd1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efd2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efd3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efddes: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kmx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vlow: float = Field(
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
# "import OverexcLimX1"
# work as well as
# "from OverexcLimX1 import OverexcLimX1".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = OverexcLimX1
