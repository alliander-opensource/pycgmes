"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovHydroR(TurbineGovernorDynamics):
    """
    Fourth order lead-lag governor and hydro turbine.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    pmax: Maximum gate opening, PU of MWbase (Pmax) (> GovHydroR.pmin).  Typical value = 1.
    pmin: Minimum gate opening, PU of MWbase (Pmin) (< GovHydroR.pmax).  Typical value = 0.
    r: Steady-state droop (R).  Typical value = 0,05.
    td: Input filter time constant (Td) (>= 0).  Typical value = 0,05.
    t1: Lead time constant 1 (T1) (>= 0).  Typical value = 1,5.
    t2: Lag time constant 1 (T2) (>= 0).  Typical value = 0,1.
    t3: Lead time constant 2 (T3) (>= 0).  Typical value = 1,5.
    t4: Lag time constant 2 (T4) (>= 0).  Typical value = 0,1.
    t5: Lead time constant 3 (T5) (>= 0).  Typical value = 0.
    t6: Lag time constant 3 (T6) (>= 0).  Typical value = 0,05.
    t7: Lead time constant 4 (T7) (>= 0).  Typical value = 0.
    t8: Lag time constant 4 (T8) (>= 0).  Typical value = 0,05.
    tp: Gate servo time constant (Tp) (>= 0).  Typical value = 0,05.
    velop: Maximum gate opening velocity (Velop).  Unit = PU / s.  Typical value = 0,2.
    velcl: Maximum gate closing velocity (Velcl).  Unit = PU / s.  Typical value = -0,2.
    ki: Integral gain (Ki).  Typical value = 0,5.
    kg: Gate servo gain (Kg).  Typical value = 2.
    gmax: Maximum governor output (Gmax) (> GovHydroR.gmin).  Typical value = 1,05.
    gmin: Minimum governor output (Gmin) (< GovHydroR.gmax).  Typical value = -0,05.
    tt: Power feedback time constant (Tt) (>= 0).  Typical value = 0.
    inputSignal: Input signal switch (Flag). true = Pe input is used false = feedback is received from CV. Flag is
      normally dependent on Tt.  If Tt is zero, Flag is set to false. If Tt is not zero, Flag is set to
      true.   Typical value = true.
    db1: Intentional dead-band width (db1).  Unit = Hz.  Typical value = 0.
    eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical value = 0.
    db2: Unintentional dead-band (db2).  Unit = MW.  Typical value = 0.
    tw: Water inertia time constant (Tw) (> 0).  Typical value = 1.
    at: Turbine gain (At).  Typical value = 1,2.
    dturb: Turbine damping factor (Dturb).  Typical value = 0,2.
    qnl: No-load turbine flow at nominal head (Qnl).  Typical value = 0,08.
    h0: Turbine nominal head (H0).  Typical value = 1.
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

    mwbase: float = 0.0  # Type #ActivePower in CIM
    pmax: float = 0.0  # Type #PU in CIM
    pmin: float = 0.0  # Type #PU in CIM
    r: float = 0.0  # Type #PU in CIM
    td: int = 0  # Type #Seconds in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    t5: int = 0  # Type #Seconds in CIM
    t6: int = 0  # Type #Seconds in CIM
    t7: int = 0  # Type #Seconds in CIM
    t8: int = 0  # Type #Seconds in CIM
    tp: int = 0  # Type #Seconds in CIM
    velop: float = 0.0  # Type #Float in CIM
    velcl: float = 0.0  # Type #Float in CIM
    ki: float = 0.0  # Type #PU in CIM
    kg: float = 0.0  # Type #PU in CIM
    gmax: float = 0.0  # Type #PU in CIM
    gmin: float = 0.0  # Type #PU in CIM
    tt: int = 0  # Type #Seconds in CIM
    inputSignal: bool = False  # Type #Boolean in CIM
    db1: float = 0.0  # Type #Frequency in CIM
    eps: float = 0.0  # Type #Frequency in CIM
    db2: float = 0.0  # Type #ActivePower in CIM
    tw: int = 0  # Type #Seconds in CIM
    at: float = 0.0  # Type #PU in CIM
    dturb: float = 0.0  # Type #PU in CIM
    qnl: float = 0.0  # Type #PU in CIM
    h0: float = 0.0  # Type #PU in CIM
    gv1: float = 0.0  # Type #PU in CIM
    pgv1: float = 0.0  # Type #PU in CIM
    gv2: float = 0.0  # Type #PU in CIM
    pgv2: float = 0.0  # Type #PU in CIM
    gv3: float = 0.0  # Type #PU in CIM
    pgv3: float = 0.0  # Type #PU in CIM
    gv4: float = 0.0  # Type #PU in CIM
    pgv4: float = 0.0  # Type #PU in CIM
    gv5: float = 0.0  # Type #PU in CIM
    pgv5: float = 0.0  # Type #PU in CIM
    gv6: float = 0.0  # Type #PU in CIM
    pgv6: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GovHydroR"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.DY.value,
            ],
            # Attributes
            "mwbase": [
                Profile.DY.value,
            ],
            "pmax": [
                Profile.DY.value,
            ],
            "pmin": [
                Profile.DY.value,
            ],
            "r": [
                Profile.DY.value,
            ],
            "td": [
                Profile.DY.value,
            ],
            "t1": [
                Profile.DY.value,
            ],
            "t2": [
                Profile.DY.value,
            ],
            "t3": [
                Profile.DY.value,
            ],
            "t4": [
                Profile.DY.value,
            ],
            "t5": [
                Profile.DY.value,
            ],
            "t6": [
                Profile.DY.value,
            ],
            "t7": [
                Profile.DY.value,
            ],
            "t8": [
                Profile.DY.value,
            ],
            "tp": [
                Profile.DY.value,
            ],
            "velop": [
                Profile.DY.value,
            ],
            "velcl": [
                Profile.DY.value,
            ],
            "ki": [
                Profile.DY.value,
            ],
            "kg": [
                Profile.DY.value,
            ],
            "gmax": [
                Profile.DY.value,
            ],
            "gmin": [
                Profile.DY.value,
            ],
            "tt": [
                Profile.DY.value,
            ],
            "inputSignal": [
                Profile.DY.value,
            ],
            "db1": [
                Profile.DY.value,
            ],
            "eps": [
                Profile.DY.value,
            ],
            "db2": [
                Profile.DY.value,
            ],
            "tw": [
                Profile.DY.value,
            ],
            "at": [
                Profile.DY.value,
            ],
            "dturb": [
                Profile.DY.value,
            ],
            "qnl": [
                Profile.DY.value,
            ],
            "h0": [
                Profile.DY.value,
            ],
            "gv1": [
                Profile.DY.value,
            ],
            "pgv1": [
                Profile.DY.value,
            ],
            "gv2": [
                Profile.DY.value,
            ],
            "pgv2": [
                Profile.DY.value,
            ],
            "gv3": [
                Profile.DY.value,
            ],
            "pgv3": [
                Profile.DY.value,
            ],
            "gv4": [
                Profile.DY.value,
            ],
            "pgv4": [
                Profile.DY.value,
            ],
            "gv5": [
                Profile.DY.value,
            ],
            "pgv5": [
                Profile.DY.value,
            ],
            "gv6": [
                Profile.DY.value,
            ],
            "pgv6": [
                Profile.DY.value,
            ],
        }
