"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovHydroIEEE2(TurbineGovernorDynamics):
    """
    IEEE hydro turbine governor model represents plants with straightforward penstock configurations and hydraulic-
      dashpot governors. Reference: IEEE Transactions on Power Apparatus and Systems, November/December 1973, Volume
      PAS-92, Number 6, Dynamic Models for Steam and Hydro Turbines in Power System Studies, page 1904.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    tg: Gate servo time constant (Tg) (>= 0).  Typical value = 0,5.
    tp: Pilot servo valve time constant (Tp) (>= 0).  Typical value = 0,03.
    uo: Maximum gate opening velocity (Uo).  Unit = PU / s.  Typical value = 0,1.
    uc: Maximum gate closing velocity (Uc) (<0).  Typical value = -0,1.
    pmax: Maximum gate opening (Pmax) (> GovHydroIEEE2.pmin).  Typical value = 1.
    pmin: Minimum gate opening (Pmin) (<GovHydroIEEE2.pmax).  Typical value = 0.
    rperm: Permanent droop (Rperm).  Typical value = 0,05.
    rtemp: Temporary droop (Rtemp).  Typical value = 0,5.
    tr: Dashpot time constant (Tr) (>= 0).  Typical value = 12.
    tw: Water inertia time constant (Tw) (>= 0).  Typical value = 2.
    kturb: Turbine gain (Kturb).  Typical value = 1.
    aturb: Turbine numerator multiplier (Aturb).  Typical value = -1.
    bturb: Turbine denominator multiplier (Bturb) (> 0).  Typical value = 0,5.
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
    tg: int = 0  # Type #Seconds in CIM
    tp: int = 0  # Type #Seconds in CIM
    uo: float = 0.0  # Type #Float in CIM
    uc: float = 0.0  # Type #Float in CIM
    pmax: float = 0.0  # Type #PU in CIM
    pmin: float = 0.0  # Type #PU in CIM
    rperm: float = 0.0  # Type #PU in CIM
    rtemp: float = 0.0  # Type #PU in CIM
    tr: int = 0  # Type #Seconds in CIM
    tw: int = 0  # Type #Seconds in CIM
    kturb: float = 0.0  # Type #PU in CIM
    aturb: float = 0.0  # Type #PU in CIM
    bturb: float = 0.0  # Type #PU in CIM
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
            ["class=GovHydroIEEE2"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "tg": [
                Profile.DY.value,
            ],
            "tp": [
                Profile.DY.value,
            ],
            "uo": [
                Profile.DY.value,
            ],
            "uc": [
                Profile.DY.value,
            ],
            "pmax": [
                Profile.DY.value,
            ],
            "pmin": [
                Profile.DY.value,
            ],
            "rperm": [
                Profile.DY.value,
            ],
            "rtemp": [
                Profile.DY.value,
            ],
            "tr": [
                Profile.DY.value,
            ],
            "tw": [
                Profile.DY.value,
            ],
            "kturb": [
                Profile.DY.value,
            ],
            "aturb": [
                Profile.DY.value,
            ],
            "bturb": [
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
