"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovHydroWPID(TurbineGovernorDynamics):
    """
    WoodwardTM PID hydro governor. [Footnote: Woodward PID hydro governors are an example of suitable products available
      commercially. This information is given for the convenience of users of this document and does not constitute
      an endorsement by IEC of these products.]

    mwbase: Base for power values  (MWbase) (> 0).  Unit = MW.
    treg: Speed detector time constant (Treg) (>= 0).
    reg: Permanent drop (Reg).
    kp: Proportional gain (Kp).  Typical value = 0,1.
    ki: Reset gain (Ki).  Typical value = 0,36.
    kd: Derivative gain (Kd).  Typical value = 1,11.
    ta: Controller time constant (Ta) (>= 0).  Typical value = 0.
    tb: Gate servo time constant (Tb) (>= 0).  Typical value = 0.
    velmax: Maximum gate opening velocity (Velmax) (> GovHydroWPID.velmin).  Unit = PU / s.  Typical value = 0.
    velmin: Maximum gate closing velocity (Velmin) (< GovHydroWPID.velmax).  Unit = PU / s.  Typical value = 0.
    gatmax: Gate opening limit maximum (Gatmax) (> GovHydroWPID.gatmin).
    gatmin: Gate opening limit minimum (Gatmin) (< GovHydroWPID.gatmax).
    tw: Water inertia time constant (Tw) (>= 0).  Typical value = 0.
    pmax: Maximum power output (Pmax) (> GovHydroWPID.pmin).
    pmin: Minimum power output (Pmin) (< GovHydroWPID.pmax).
    d: Turbine damping factor (D).  Unit = delta P / delta speed.
    gv3: Gate position 3 (Gv3) (= 1,0).
    gv1: Gate position 1 (Gv1).
    pgv1: Output at Gv1 PU of MWbase (Pgv1).
    gv2: Gate position 2 (Gv2).
    pgv2: Output at Gv2 PU of MWbase (Pgv2).
    pgv3: Output at Gv3 PU of MWbase (Pgv3).
    """

    mwbase: float = 0.0  # Type #ActivePower in CIM
    treg: int = 0  # Type #Seconds in CIM
    reg: float = 0.0  # Type #PU in CIM
    kp: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #PU in CIM
    kd: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    tb: int = 0  # Type #Seconds in CIM
    velmax: float = 0.0  # Type #PU in CIM
    velmin: float = 0.0  # Type #PU in CIM
    gatmax: float = 0.0  # Type #PU in CIM
    gatmin: float = 0.0  # Type #PU in CIM
    tw: int = 0  # Type #Seconds in CIM
    pmax: float = 0.0  # Type #PU in CIM
    pmin: float = 0.0  # Type #PU in CIM
    d: float = 0.0  # Type #PU in CIM
    gv3: float = 0.0  # Type #PU in CIM
    gv1: float = 0.0  # Type #PU in CIM
    pgv1: float = 0.0  # Type #PU in CIM
    gv2: float = 0.0  # Type #PU in CIM
    pgv2: float = 0.0  # Type #PU in CIM
    pgv3: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GovHydroWPID"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "treg": [
                Profile.DY.value,
            ],
            "reg": [
                Profile.DY.value,
            ],
            "kp": [
                Profile.DY.value,
            ],
            "ki": [
                Profile.DY.value,
            ],
            "kd": [
                Profile.DY.value,
            ],
            "ta": [
                Profile.DY.value,
            ],
            "tb": [
                Profile.DY.value,
            ],
            "velmax": [
                Profile.DY.value,
            ],
            "velmin": [
                Profile.DY.value,
            ],
            "gatmax": [
                Profile.DY.value,
            ],
            "gatmin": [
                Profile.DY.value,
            ],
            "tw": [
                Profile.DY.value,
            ],
            "pmax": [
                Profile.DY.value,
            ],
            "pmin": [
                Profile.DY.value,
            ],
            "d": [
                Profile.DY.value,
            ],
            "gv3": [
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
            "pgv3": [
                Profile.DY.value,
            ],
        }
