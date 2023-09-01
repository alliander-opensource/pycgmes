"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovHydro2(TurbineGovernorDynamics):
    """
    IEEE hydro turbine governor with straightforward penstock configuration and hydraulic-dashpot governor.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    tg: Gate servo time constant (Tg) (> 0).  Typical value = 0,5.
    tp: Pilot servo valve time constant (Tp) (>= 0).  Typical value = 0,03.
    uo: Maximum gate opening velocity (Uo).  Unit = PU / s.  Typical value = 0,1.
    uc: Maximum gate closing velocity (Uc) (< 0).  Unit = PU / s.   Typical value = -0,1.
    pmax: Maximum gate opening (Pmax) (> GovHydro2.pmin).  Typical value = 1.
    pmin: Minimum gate opening (Pmin) (< GovHydro2.pmax).  Typical value = 0.
    rperm: Permanent droop (Rperm).  Typical value = 0,05.
    rtemp: Temporary droop (Rtemp).  Typical value = 0,5.
    tr: Dashpot time constant (Tr) (>= 0).  Typical value = 12.
    tw: Water inertia time constant (Tw) (>= 0).  Typical value = 2.
    kturb: Turbine gain (Kturb).  Typical value = 1.
    aturb: Turbine numerator multiplier (Aturb).  Typical value = -1.
    bturb: Turbine denominator multiplier (Bturb) (> 0).  Typical value = 0,5.
    db1: Intentional deadband width (db1).  Unit = Hz.  Typical value = 0.
    eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical value = 0.
    db2: Unintentional deadband (db2).  Unit = MW.  Typical value = 0.
    gv1: Nonlinear gain point 1, PU gv (Gv1).  Typical value = 0.
    pgv1: Nonlinear gain point 1, PU power (Pgv1).  Typical value = 0.
    gv2: Nonlinear gain point 2, PU gv (Gv2).  Typical value = 0.
    pgv2: Nonlinear gain point 2, PU power (Pgv2).  Typical value = 0.
    gv3: Nonlinear gain point 3, PU gv (Gv3).  Typical value = 0.
    pgv3: Nonlinear gain point 3, PU power (Pgv3).  Typical value = 0.
    gv4: Nonlinear gain point 4, PU gv (Gv4).  Typical value = 0.
    pgv4: Nonlinear gain point 4, PU power (Pgv4).  Typical value = 0.
    gv5: Nonlinear gain point 5, PU gv (Gv5).  Typical value = 0.
    pgv5: Nonlinear gain point 5, PU power (Pgv5).  Typical value = 0.
    gv6: Nonlinear gain point 6, PU gv (Gv6).  Typical value = 0.
    pgv6: Nonlinear gain point 6, PU power (Pgv6).  Typical value = 0.
    """

    mwbase: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tg: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tp: int = Field(
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

    rperm: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rtemp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tr: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tw: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kturb: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    aturb: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    bturb: float = Field(
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

    db2: float = Field(
        default=0.0,
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
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
