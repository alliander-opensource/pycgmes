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
class GovGAST(TurbineGovernorDynamics, ModuleType):
    """
    Single shaft gas turbine.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    r: Permanent droop (R) (>0). Typical value = 0,04.
    t1: Governor mechanism time constant (T1) (>= 0).  T1 represents the natural valve positioning time constant of the
      governor for small disturbances, as seen when rate limiting is not in effect.  Typical value = 0,5.
    t2: Turbine power time constant (T2) (>= 0).  T2 represents delay due to internal energy storage of the gas turbine
      engine. T2 can be used to give a rough approximation to the delay associated with acceleration of the
      compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of a free power
      turbine of an aero-derivative unit, for example.  Typical value = 0,5.
    t3: Turbine exhaust temperature time constant (T3) (>= 0).  Typical value = 3.
    at: Ambient temperature load limit (Load Limit).  Typical value = 1.
    kt: Temperature limiter gain (Kt).  Typical value = 3.
    vmax: Maximum turbine power, PU of MWbase (Vmax) (> GovGAST.vmin).  Typical value = 1.
    vmin: Minimum turbine power, PU of MWbase (Vmin) (< GovGAST.vmax).  Typical value = 0.
    dturb: Turbine damping factor (Dturb).  Typical value = 0,18.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return GovGAST(*args, **kwargs)

    mwbase: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    r: float = Field(
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

    t3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    at: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kt: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dturb: float = Field(
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
# "import GovGAST"
# work as well as
# "from GovGAST import GovGAST".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = GovGAST
