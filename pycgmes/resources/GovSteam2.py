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

from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovSteam2(TurbineGovernorDynamics, ModuleType):
    """
    Simplified governor.

    k: Governor gain (reciprocal of droop) (K).  Typical value = 20.
    dbf: Frequency deadband (DBF).  Typical value = 0.
    t1: Governor lag time constant (T1) (> 0).  Typical value = 0,45.
    t2: Governor lead time constant (T2) (>= 0).  Typical value = 0.
    pmax: Maximum fuel flow (PMAX) (> GovSteam2.pmin).  Typical value = 1.
    pmin: Minimum fuel flow (PMIN) (< GovSteam2.pmax).  Typical value = 0.
    mxef: Fuel flow maximum positive error value (MXEF).  Typical value = 1.
    mnef: Fuel flow maximum negative error value (MNEF).  Typical value = -1.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return GovSteam2(*args, **kwargs)

    k: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dbf: float = Field(
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

    t2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    mxef: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    mnef: float = Field(
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
# "import GovSteam2"
# work as well as
# "from GovSteam2 import GovSteam2".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = GovSteam2
