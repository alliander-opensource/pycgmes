"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass
class GovHydro3(TurbineGovernorDynamics):
    """
    Modified IEEE hydro governor-turbine. This model differs from that defined in the IEEE modelling guideline paper in
      that the limits on gate position and velocity do not permit "wind up" of the upstream signals.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    pmax: Maximum gate opening, PU of MWbase (Pmax) (> GovHydro3.pmin).  Typical value = 1.
    pmin: Minimum gate opening, PU of MWbase (Pmin) (< GovHydro3.pmax).  Typical value = 0.
    governorControl: Governor control flag (Cflag). true = PID control is active false = double derivative control is
      active. Typical value = true.
    rgate: Steady-state droop, PU, for governor output feedback (Rgate).  Typical value = 0.
    relec: Steady-state droop, PU, for electrical power feedback (Relec).  Typical value = 0,05.
    td: Input filter time constant (Td) (>= 0).  Typical value = 0,05.
    tf: Washout time constant (Tf) (>= 0).  Typical value = 0,1.
    tp: Gate servo time constant (Tp) (>= 0).  Typical value = 0,05.
    velop: Maximum gate opening velocity (Velop).  Unit = PU / s. Typical value = 0,2.
    velcl: Maximum gate closing velocity (Velcl).  Unit = PU / s.  Typical value = -0,2.
    k1: Derivative gain (K1).  Typical value = 0,01.
    k2: Double derivative gain, if Cflag = -1 (K2).  Typical value = 2,5.
    ki: Integral gain (Ki).  Typical value = 0,5.
    kg: Gate servo gain (Kg).  Typical value = 2.
    tt: Power feedback time constant (Tt) (>= 0).  Typical value = 0,2.
    db1: Intentional dead-band width (db1).  Unit = Hz.  Typical value = 0.
    eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical value = 0.
    db2: Unintentional dead-band (db2).  Unit = MW.  Typical value = 0.
    tw: Water inertia time constant (Tw) (>= 0).  If = 0, block is bypassed.  Typical value = 1.
    at: Turbine gain (At) (>0).  Typical value = 1,2.
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    mwbase: float = 0.0  # Type #ActivePower in CIM
    pmax: float = 0.0  # Type #PU in CIM
    pmin: float = 0.0  # Type #PU in CIM
    governorControl: bool = False  # Type #Boolean in CIM
    rgate: float = 0.0  # Type #PU in CIM
    relec: float = 0.0  # Type #PU in CIM
    td: int = 0  # Type #Seconds in CIM
    tf: int = 0  # Type #Seconds in CIM
    tp: int = 0  # Type #Seconds in CIM
    velop: float = 0.0  # Type #Float in CIM
    velcl: float = 0.0  # Type #Float in CIM
    k1: float = 0.0  # Type #PU in CIM
    k2: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #PU in CIM
    kg: float = 0.0  # Type #PU in CIM
    tt: int = 0  # Type #Seconds in CIM
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
        str_ = "class=GovHydro3\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.DY.value,
            ],
            # Attributes
            "mwbase": [
                self.profiles.DY.value,
            ],
            "pmax": [
                self.profiles.DY.value,
            ],
            "pmin": [
                self.profiles.DY.value,
            ],
            "governorControl": [
                self.profiles.DY.value,
            ],
            "rgate": [
                self.profiles.DY.value,
            ],
            "relec": [
                self.profiles.DY.value,
            ],
            "td": [
                self.profiles.DY.value,
            ],
            "tf": [
                self.profiles.DY.value,
            ],
            "tp": [
                self.profiles.DY.value,
            ],
            "velop": [
                self.profiles.DY.value,
            ],
            "velcl": [
                self.profiles.DY.value,
            ],
            "k1": [
                self.profiles.DY.value,
            ],
            "k2": [
                self.profiles.DY.value,
            ],
            "ki": [
                self.profiles.DY.value,
            ],
            "kg": [
                self.profiles.DY.value,
            ],
            "tt": [
                self.profiles.DY.value,
            ],
            "db1": [
                self.profiles.DY.value,
            ],
            "eps": [
                self.profiles.DY.value,
            ],
            "db2": [
                self.profiles.DY.value,
            ],
            "tw": [
                self.profiles.DY.value,
            ],
            "at": [
                self.profiles.DY.value,
            ],
            "dturb": [
                self.profiles.DY.value,
            ],
            "qnl": [
                self.profiles.DY.value,
            ],
            "h0": [
                self.profiles.DY.value,
            ],
            "gv1": [
                self.profiles.DY.value,
            ],
            "pgv1": [
                self.profiles.DY.value,
            ],
            "gv2": [
                self.profiles.DY.value,
            ],
            "pgv2": [
                self.profiles.DY.value,
            ],
            "gv3": [
                self.profiles.DY.value,
            ],
            "pgv3": [
                self.profiles.DY.value,
            ],
            "gv4": [
                self.profiles.DY.value,
            ],
            "pgv4": [
                self.profiles.DY.value,
            ],
            "gv5": [
                self.profiles.DY.value,
            ],
            "pgv5": [
                self.profiles.DY.value,
            ],
            "gv6": [
                self.profiles.DY.value,
            ],
            "pgv6": [
                self.profiles.DY.value,
            ],
        }
