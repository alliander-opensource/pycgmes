"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovHydroDD(TurbineGovernorDynamics):
    """
    Double derivative hydro governor and turbine.

    mwbase: Base for power values (MWbase) (>0).  Unit = MW.
    pmax: Maximum gate opening, PU of MWbase (Pmax) (> GovHydroDD.pmin).  Typical value = 1.
    pmin: Minimum gate opening, PU of MWbase (Pmin) (> GovHydroDD.pmax).  Typical value = 0.
    r: Steady state droop (R).  Typical value = 0,05.
    td: Input filter time constant (Td) (>= 0).  If = 0, block is bypassed.  Typical value = 0.
    tf: Washout time constant (Tf) (>= 0).  Typical value = 0,1.
    tp: Gate servo time constant (Tp) (>= 0).  If = 0, block is bypassed.  Typical value = 0,35.
    velop: Maximum gate opening velocity (Velop).  Unit = PU / s.  Typical value = 0,09.
    velcl: Maximum gate closing velocity (Velcl).  Unit = PU / s.  Typical value = -0,14.
    k1: Single derivative gain (K1).  Typical value = 3,6.
    k2: Double derivative gain (K2).  Typical value = 0,2.
    ki: Integral gain (Ki).  Typical value = 1.
    kg: Gate servo gain (Kg).  Typical value = 3.
    tturb: Turbine time constant (Tturb)  (>= 0).  See parameter detail 3.  Typical value = 0,8.
    aturb: Turbine numerator multiplier (Aturb) (see parameter detail 3).  Typical value = -1.
    bturb: Turbine denominator multiplier (Bturb) (see parameter detail 3).  Typical value = 0,5.
    tt: Power feedback time constant (Tt) (>= 0).  If = 0, block is bypassed.  Typical value = 0,02.
    db1: Intentional dead-band width (db1).  Unit = Hz.  Typical value = 0.
    eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical value = 0.
    db2: Unintentional dead-band (db2).  Unit = MW.  Typical value = 0.
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
    gmax: Maximum gate opening (Gmax) (> GovHydroDD.gmin).  Typical value = 0.
    gmin: Minimum gate opening (Gmin) (< GovHydroDD.gmax).  Typical value = 0.
    inputSignal: Input signal switch (Flag).  true = Pe input is used false = feedback is received from CV. Flag is
      normally dependent on Tt.  If Tt is zero, Flag is set to false. If Tt is not zero, Flag is set to
      true.   Typical value = true.
    """

    mwbase: float = Field(
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

    r: float = Field(
        default=0.0,
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

    tf: int = Field(
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

    velop: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    velcl: float = Field(
        default=0.0,
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

    ki: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kg: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tturb: int = Field(
        default=0,
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

    tt: int = Field(
        default=0,
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

    gmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    inputSignal: bool = Field(
        default=False,
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
