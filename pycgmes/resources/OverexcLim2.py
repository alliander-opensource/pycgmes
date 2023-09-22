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
class OverexcLim2(OverexcitationLimiterDynamics, ModuleType):
    """
    Different from LimIEEEOEL, LimOEL2 has a fixed pickup threshold and reduces the excitation set-point by means of a
      non-windup integral regulator. Irated is the rated machine excitation current (calculated from nameplate
      conditions: Vnom, Pnom, CosPhinom).

    koi: Gain Over excitation limiter (KOI).  Typical value = 0,1.
    voimax: Maximum error signal (VOIMAX) (> OverexcLim2.voimin).  Typical value = 0.
    voimin: Minimum error signal (VOIMIN) (< OverexcLim2.voimax).  Typical value = -9999.
    ifdlim: Limit value of rated field current (IFDLIM).  Typical value = 1,05.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return OverexcLim2(*args, **kwargs)

    koi: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    voimax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    voimin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ifdlim: float = Field(
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
# "import OverexcLim2"
# work as well as
# "from OverexcLim2 import OverexcLim2".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = OverexcLim2
