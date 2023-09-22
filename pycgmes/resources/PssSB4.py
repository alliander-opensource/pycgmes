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

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass(config=DataclassConfig)
class PssSB4(PowerSystemStabilizerDynamics, ModuleType):
    """
    Power sensitive stabilizer model.

    tt: Time constant (Tt) (>= 0).  Typical value = 0,18.
    kx: Gain (Kx).  Typical value = 2,7.
    tx2: Time constant (Tx2) (>= 0).  Typical value = 5,0.
    ta: Time constant (Ta) (>= 0).  Typical value = 0,37.
    tx1: Reset time constant (Tx1) (>= 0).  Typical value = 0,035.
    tb: Time constant (Tb) (>= 0).  Typical value = 0,37.
    tc: Time constant (Tc) (>= 0).  Typical value = 0,035.
    td: Time constant (Td) (>= 0).  Typical value = 0,0.
    te: Time constant (Te) (>= 0).  Typical value = 0,0169.
    vsmax: Limiter (Vsmax) (> PssSB4.vsmin).  Typical value = 0,062.
    vsmin: Limiter (Vsmin) (< PssSB4.vsmax).  Typical value = -0,062.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return PssSB4(*args, **kwargs)

    tt: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tx2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ta: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tx1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tb: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tc: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    td: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    te: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vsmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vsmin: float = Field(
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
# "import PssSB4"
# work as well as
# "from PssSB4 import PssSB4".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = PssSB4
