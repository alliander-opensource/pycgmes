"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovHydroPID2(TurbineGovernorDynamics):
    """
    Hydro turbine and governor. Represents plants with straightforward penstock configurations and "three term" electro-
      hydraulic governors (i.e. WoodwardTM electronic). [Footnote: Woodward electronic governors are an example of
      suitable products available commercially. This information is given for the convenience of users of this
      document and does not constitute an endorsement by IEC of these products.]

    mwbase: Base for power values (MWbase) (>0).  Unit = MW.
    treg: Speed detector time constant (Treg) (>= 0).  Typical value = 0.
    rperm: Permanent drop (Rperm).  Typical value = 0.
    kp: Proportional gain (Kp).  Typical value = 0.
    ki: Reset gain (Ki).  Unit = PU/s.  Typical value = 0.
    kd: Derivative gain (Kd).  Typical value = 0.
    ta: Controller time constant (Ta) (>= 0).  Typical value = 0.
    tb: Gate servo time constant (Tb) (> 0).
    velmax: Maximum gate opening velocity (Velmax) (< GovHydroPID2.velmin).  Unit = PU / s.  Typical value = 0.
    velmin: Maximum gate closing velocity (Velmin) (> GovHydroPID2.velmax).  Unit = PU / s.  Typical value = 0.
    gmax: Maximum gate opening (Gmax) (> GovHydroPID2.gmin).  Typical value = 0.
    gmin: Minimum gate opening (Gmin) (> GovHydroPID2.gmax).  Typical value = 0.
    tw: Water inertia time constant (Tw) (>= 0).  Typical value = 0.
    d: Turbine damping factor (D).  Unit = delta P / delta speed.  Typical value = 0.
    g0: Gate opening at speed no load (G0).  Typical value = 0.
    g1: Intermediate gate opening (G1).  Typical value = 0.
    p1: Power at gate opening G1 (P1).  Typical value = 0.
    g2: Intermediate gate opening (G2).  Typical value = 0.
    p2: Power at gate opening G2 (P2).  Typical value = 0.
    p3: Power at full opened gate (P3).  Typical value = 0.
    atw: Factor multiplying Tw (Atw).  Typical value = 0.
    feedbackSignal: Feedback signal type flag (Flag). true = use gate position feedback signal false = use Pe.
    """

    mwbase: float = 0.0  # Type #ActivePower in CIM
    treg: int = 0  # Type #Seconds in CIM
    rperm: float = 0.0  # Type #PU in CIM
    kp: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #Float in CIM
    kd: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    tb: int = 0  # Type #Seconds in CIM
    velmax: float = 0.0  # Type #Float in CIM
    velmin: float = 0.0  # Type #Float in CIM
    gmax: float = 0.0  # Type #PU in CIM
    gmin: float = 0.0  # Type #PU in CIM
    tw: int = 0  # Type #Seconds in CIM
    d: float = 0.0  # Type #PU in CIM
    g0: float = 0.0  # Type #PU in CIM
    g1: float = 0.0  # Type #PU in CIM
    p1: float = 0.0  # Type #PU in CIM
    g2: float = 0.0  # Type #PU in CIM
    p2: float = 0.0  # Type #PU in CIM
    p3: float = 0.0  # Type #PU in CIM
    atw: float = 0.0  # Type #PU in CIM
    feedbackSignal: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GovHydroPID2"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "rperm": [
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
            "gmax": [
                Profile.DY.value,
            ],
            "gmin": [
                Profile.DY.value,
            ],
            "tw": [
                Profile.DY.value,
            ],
            "d": [
                Profile.DY.value,
            ],
            "g0": [
                Profile.DY.value,
            ],
            "g1": [
                Profile.DY.value,
            ],
            "p1": [
                Profile.DY.value,
            ],
            "g2": [
                Profile.DY.value,
            ],
            "p2": [
                Profile.DY.value,
            ],
            "p3": [
                Profile.DY.value,
            ],
            "atw": [
                Profile.DY.value,
            ],
            "feedbackSignal": [
                Profile.DY.value,
            ],
        }
