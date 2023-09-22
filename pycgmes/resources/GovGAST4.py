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
class GovGAST4(TurbineGovernorDynamics, ModuleType):
    """
    Generic turbogas.

    bp: Droop (bp).  Typical value = 0,05.
    ty: Time constant of fuel valve positioner (Ty) (>= 0).  Typical value = 0,1.
    ta: Maximum gate opening velocity (TA) (>= 0).  Typical value = 3.
    tc: Maximum gate closing velocity (TC) (>= 0).  Typical value = 0,5.
    tcm: Fuel control time constant (Tcm) (>= 0).  Typical value = 0,1.
    ktm: Compressor gain (Ktm).  Typical value = 0.
    tm: Compressor discharge volume time constant (Tm) (>= 0).  Typical value = 0,2.
    rymx: Maximum valve opening (RYMX).  Typical value = 1,1.
    rymn: Minimum valve opening (RYMN).  Typical value = 0.
    mxef: Fuel flow maximum positive error value (MXef).  Typical value = 0,05.
    mnef: Fuel flow maximum negative error value (MNef).  Typical value = -0,05.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return GovGAST4(*args, **kwargs)

    bp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ty: int = Field(
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

    tc: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tcm: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ktm: float = Field(
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

    rymx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rymn: float = Field(
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
# "import GovGAST4"
# work as well as
# "from GovGAST4 import GovGAST4".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = GovGAST4
