"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass
class GovHydro4(TurbineGovernorDynamics):
    """
    Hydro turbine and governor. Represents plants with straight-forward penstock configurations and hydraulic governors
      of the traditional 'dashpot' type.  This model can be used to represent simple, Francis/Pelton or Kaplan
      turbines.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    tg: Gate servo time constant (Tg) (> 0).  Typical value = 0,5.
    tp: Pilot servo time constant (Tp) (>= 0).  Typical value = 0,1.
    uo: Max gate opening velocity (Uo).  Typical value = 0,2.
    uc: Max gate closing velocity (Uc).  Typical value = 0,2.
    gmax: Maximum gate opening, PU of MWbase (Gmax) (> GovHydro4.gmin).  Typical value = 1.
    gmin: Minimum gate opening, PU of MWbase (Gmin) (< GovHydro4.gmax).  Typical value = 0.
    rperm: Permanent droop (Rperm) (>= 0).  Typical value = 0,05.
    rtemp: Temporary droop (Rtemp) (>= 0).  Typical value = 0,3.
    tr: Dashpot time constant (Tr) (>= 0).  Typical value = 5.
    tw: Water inertia time constant (Tw) (> 0).  Typical value = 1.
    at: Turbine gain (At).  Typical value = 1,2.
    dturb: Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU).  Typical value for simple
      = 0,5, Francis/Pelton = 1,1, Kaplan = 1,1.
    hdam: Head available at dam (hdam).  Typical value = 1.
    qnl: No-load flow at nominal head (Qnl). Typical value for simple = 0,08, Francis/Pelton = 0, Kaplan = 0.
    db1: Intentional deadband width (db1).  Unit = Hz.  Typical value = 0.
    eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical value = 0.
    db2: Unintentional dead-band (db2).  Unit = MW.  Typical value = 0.
    gv0: Nonlinear gain point 0, PU gv (Gv0) (= 0 for simple).  Typical for Francis/Pelton = 0,1, Kaplan = 0,1.
    pgv0: Nonlinear gain point 0, PU power (Pgv0) (= 0 for simple).  Typical value = 0.
    gv1: Nonlinear gain point 1, PU gv (Gv1) (= 0 for simple, > GovHydro4.gv0 for Francis/Pelton and Kaplan). Typical
      value for Francis/Pelton = 0,4, Kaplan = 0,4.
    pgv1: Nonlinear gain point 1, PU power (Pgv1) (= 0 for simple). Typical value for Francis/Pelton = 0,42, Kaplan =
      0,35.
    gv2: Nonlinear gain point 2, PU gv (Gv2) (= 0 for simple, > GovHydro4.gv1 for Francis/Pelton and Kaplan). Typical
      value for Francis/Pelton = 0,5, Kaplan = 0,5.
    pgv2: Nonlinear gain point 2, PU power (Pgv2) (= 0 for simple). Typical value for Francis/Pelton = 0,56, Kaplan =
      0,468.
    gv3: Nonlinear gain point 3, PU gv (Gv3)  (= 0 for simple, > GovHydro4.gv2 for Francis/Pelton and Kaplan). Typical
      value for Francis/Pelton = 0,7, Kaplan = 0,7.
    pgv3: Nonlinear gain point 3, PU power (Pgv3) (= 0 for simple). Typical value for Francis/Pelton = 0,8, Kaplan =
      0,796.
    gv4: Nonlinear gain point 4, PU gv (Gv4)  (= 0 for simple, > GovHydro4.gv3 for Francis/Pelton and Kaplan). Typical
      value for  Francis/Pelton = 0,8, Kaplan = 0,8.
    pgv4: Nonlinear gain point 4, PU power (Pgv4) (= 0 for simple). Typical value for Francis/Pelton = 0,9, Kaplan =
      0,917.
    gv5: Nonlinear gain point 5, PU gv (Gv5)  (= 0 for simple, < 1 and > GovHydro4.gv4 for Francis/Pelton and Kaplan).
      Typical value for Francis/Pelton = 0,9, Kaplan = 0,9.
    pgv5: Nonlinear gain point 5, PU power (Pgv5) (= 0 for simple).  Typical value for Francis/Pelton = 0,97, Kaplan =
      0,99.
    bgv0: Kaplan blade servo point 0 (Bgv0) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 0.
    bgv1: Kaplan blade servo point 1 (Bgv1) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 0.
    bgv2: Kaplan blade servo point 2 (Bgv2) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 0,1.
    bgv3: Kaplan blade servo point 3 (Bgv3) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 0,667.
    bgv4: Kaplan blade servo point 4 (Bgv4) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 0,9.
    bgv5: Kaplan blade servo point 5 (Bgv5) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 1.
    bmax: Maximum blade adjustment factor (Bmax)  (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan =
      1,1276.
    tblade: Blade servo time constant (Tblade) (>= 0).  Typical value = 100.
    model: The kind of model being represented (simple, Francis/Pelton or Kaplan).
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    mwbase: float = 0.0  # Type #ActivePower in CIM
    tg: int = 0  # Type #Seconds in CIM
    tp: int = 0  # Type #Seconds in CIM
    uo: float = 0.0  # Type #Float in CIM
    uc: float = 0.0  # Type #Float in CIM
    gmax: float = 0.0  # Type #PU in CIM
    gmin: float = 0.0  # Type #PU in CIM
    rperm: int = 0  # Type #Seconds in CIM
    rtemp: int = 0  # Type #Seconds in CIM
    tr: int = 0  # Type #Seconds in CIM
    tw: int = 0  # Type #Seconds in CIM
    at: float = 0.0  # Type #PU in CIM
    dturb: float = 0.0  # Type #PU in CIM
    hdam: float = 0.0  # Type #PU in CIM
    qnl: float = 0.0  # Type #PU in CIM
    db1: float = 0.0  # Type #Frequency in CIM
    eps: float = 0.0  # Type #Frequency in CIM
    db2: float = 0.0  # Type #ActivePower in CIM
    gv0: float = 0.0  # Type #PU in CIM
    pgv0: float = 0.0  # Type #PU in CIM
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
    bgv0: float = 0.0  # Type #PU in CIM
    bgv1: float = 0.0  # Type #PU in CIM
    bgv2: float = 0.0  # Type #PU in CIM
    bgv3: float = 0.0  # Type #PU in CIM
    bgv4: float = 0.0  # Type #PU in CIM
    bgv5: float = 0.0  # Type #PU in CIM
    bmax: float = 0.0  # Type #Float in CIM
    tblade: int = 0  # Type #Seconds in CIM
    model: Optional[str] = None  # Type M:1..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=GovHydro4\n"
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
            "tg": [
                self.profiles.DY.value,
            ],
            "tp": [
                self.profiles.DY.value,
            ],
            "uo": [
                self.profiles.DY.value,
            ],
            "uc": [
                self.profiles.DY.value,
            ],
            "gmax": [
                self.profiles.DY.value,
            ],
            "gmin": [
                self.profiles.DY.value,
            ],
            "rperm": [
                self.profiles.DY.value,
            ],
            "rtemp": [
                self.profiles.DY.value,
            ],
            "tr": [
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
            "hdam": [
                self.profiles.DY.value,
            ],
            "qnl": [
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
            "gv0": [
                self.profiles.DY.value,
            ],
            "pgv0": [
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
            "bgv0": [
                self.profiles.DY.value,
            ],
            "bgv1": [
                self.profiles.DY.value,
            ],
            "bgv2": [
                self.profiles.DY.value,
            ],
            "bgv3": [
                self.profiles.DY.value,
            ],
            "bgv4": [
                self.profiles.DY.value,
            ],
            "bgv5": [
                self.profiles.DY.value,
            ],
            "bmax": [
                self.profiles.DY.value,
            ],
            "tblade": [
                self.profiles.DY.value,
            ],
            "model": [
                self.profiles.DY.value,
            ],
        }
