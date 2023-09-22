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
class GovSteam1(TurbineGovernorDynamics, ModuleType):
    """
    Steam turbine governor, based on the GovSteamIEEE1 (with optional deadband and nonlinear valve gain added).

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    k: Governor gain (reciprocal of droop) (K) (> 0).  Typical value = 25.
    t1: Governor lag time constant (T1) (>= 0).  Typical value = 0.
    t2: Governor lead time constant (T2) (>= 0).  Typical value = 0.
    t3: Valve positioner time constant (T3) (> 0).  Typical value = 0,1.
    uo: Maximum valve opening velocity (Uo) (> 0).  Unit = PU / s.  Typical value = 1.
    uc: Maximum valve closing velocity (Uc) (< 0).  Unit = PU / s.  Typical value = -10.
    pmax: Maximum valve opening (Pmax) (> GovSteam1.pmin).  Typical value = 1.
    pmin: Minimum valve opening (Pmin) (>= 0 and < GovSteam1.pmax).  Typical value = 0.
    t4: Inlet piping/steam bowl time constant (T4) (>= 0).  Typical value = 0,3.
    k1: Fraction of HP shaft power after first boiler pass (K1).  Typical value = 0,2.
    k2: Fraction of LP shaft power after first boiler pass (K2).  Typical value = 0.
    t5: Time constant of second boiler pass (T5) (>= 0).  Typical value = 5.
    k3: Fraction of HP shaft power after second boiler pass (K3).  Typical value = 0,3.
    k4: Fraction of LP shaft power after second boiler pass (K4).  Typical value = 0.
    t6: Time constant of third boiler pass (T6) (>= 0).  Typical value = 0,5.
    k5: Fraction of HP shaft power after third boiler pass (K5).  Typical value = 0,5.
    k6: Fraction of LP shaft power after third boiler pass (K6).  Typical value = 0.
    t7: Time constant of fourth boiler pass (T7) (>= 0).  Typical value = 0.
    k7: Fraction of HP shaft power after fourth boiler pass (K7).  Typical value = 0.
    k8: Fraction of LP shaft power after fourth boiler pass (K8).  Typical value = 0.
    db1: Intentional deadband width (db1).  Unit = Hz.  Typical value = 0.
    eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical value = 0.
    sdb1: Intentional deadband indicator. true = intentional deadband is applied false = intentional deadband is not
      applied. Typical value = true.
    sdb2: Unintentional deadband location. true = intentional deadband is applied before point `A` false = intentional
      deadband is applied after point `A`. Typical value = true.
    db2: Unintentional deadband (db2).  Unit = MW.  Typical value = 0.
    valve: Nonlinear valve characteristic. true = nonlinear valve characteristic is used false = nonlinear valve
      characteristic is not used. Typical value = true.
    gv1: Nonlinear gain valve position point 1 (GV1).  Typical value = 0.
    pgv1: Nonlinear gain power value point 1 (Pgv1).  Typical value = 0.
    gv2: Nonlinear gain valve position point 2 (GV2).  Typical value = 0,4.
    pgv2: Nonlinear gain power value point 2 (Pgv2).  Typical value = 0,75.
    gv3: Nonlinear gain valve position point 3 (GV3).  Typical value = 0,5.
    pgv3: Nonlinear gain power value point 3 (Pgv3).  Typical value = 0,91.
    gv4: Nonlinear gain valve position point 4 (GV4).  Typical value = 0,6.
    pgv4: Nonlinear gain power value point 4 (Pgv4).  Typical value = 0,98.
    gv5: Nonlinear gain valve position point 5 (GV5).  Typical value = 1.
    pgv5: Nonlinear gain power value point 5 (Pgv5).  Typical value = 1.
    gv6: Nonlinear gain valve position point 6 (GV6).  Typical value = 0.
    pgv6: Nonlinear gain power value point 6 (Pgv6).  Typical value = 0.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return GovSteam1(*args, **kwargs)

    mwbase: float = Field(
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

    uo: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    uc: float = Field(
        default=0.0,
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

    t4: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t5: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k4: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t6: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k5: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k6: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t7: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k7: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k8: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    db1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    eps: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    sdb1: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    sdb2: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    db2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    valve: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    gv1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pgv1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gv2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pgv2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gv3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pgv3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gv4: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pgv4: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gv5: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pgv5: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gv6: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pgv6: float = Field(
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
# "import GovSteam1"
# work as well as
# "from GovSteam1 import GovSteam1".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = GovSteam1
