"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics


@dataclass(config=DataclassConfig)
class UnderexcLimIEEE1(UnderexcitationLimiterDynamics):
    """
    Type UEL1 model which has a circular limit boundary when plotted in terms of machine reactive power vs. real power
      output. Reference: IEEE UEL1 421.5-2005, 10.1.

    kur: UEL radius setting (KUR).  Typical value = 1,95.
    kuc: UEL centre setting (KUC).  Typical value = 1,38.
    kuf: UEL excitation system stabilizer gain (KUF).  Typical value = 3,3.
    vurmax: UEL maximum limit for radius phasor magnitude (VURMAX).  Typical value = 5,8.
    vucmax: UEL maximum limit for operating point phasor magnitude (VUCMAX).  Typical value = 5,8.
    kui: UEL integral gain (KUI).  Typical value = 0.
    kul: UEL proportional gain (KUL).  Typical value = 100.
    vuimax: UEL integrator output maximum limit (VUIMAX) (> UnderexcLimIEEE1.vuimin).
    vuimin: UEL integrator output minimum limit (VUIMIN) (< UnderexcLimIEEE1.vuimax).
    tu1: UEL lead time constant (TU1) (>= 0).  Typical value = 0.
    tu2: UEL lag time constant (TU2) (>= 0).  Typical value = 0,05.
    tu3: UEL lead time constant (TU3) (>= 0).  Typical value = 0.
    tu4: UEL lag time constant (TU4) (>= 0).  Typical value = 0.
    vulmax: UEL output maximum limit (VULMAX) (> UnderexcLimIEEE1.vulmin).  Typical value = 18.
    vulmin: UEL output minimum limit (VULMIN) (< UnderexcLimIEEE1.vulmax).  Typical value = -18.
    """

    kur: float = 0.0  # Type #PU in CIM
    kuc: float = 0.0  # Type #PU in CIM
    kuf: float = 0.0  # Type #PU in CIM
    vurmax: float = 0.0  # Type #PU in CIM
    vucmax: float = 0.0  # Type #PU in CIM
    kui: float = 0.0  # Type #PU in CIM
    kul: float = 0.0  # Type #PU in CIM
    vuimax: float = 0.0  # Type #PU in CIM
    vuimin: float = 0.0  # Type #PU in CIM
    tu1: int = 0  # Type #Seconds in CIM
    tu2: int = 0  # Type #Seconds in CIM
    tu3: int = 0  # Type #Seconds in CIM
    tu4: int = 0  # Type #Seconds in CIM
    vulmax: float = 0.0  # Type #PU in CIM
    vulmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=UnderexcLimIEEE1"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "kur": [
                Profile.DY.value,
            ],
            "kuc": [
                Profile.DY.value,
            ],
            "kuf": [
                Profile.DY.value,
            ],
            "vurmax": [
                Profile.DY.value,
            ],
            "vucmax": [
                Profile.DY.value,
            ],
            "kui": [
                Profile.DY.value,
            ],
            "kul": [
                Profile.DY.value,
            ],
            "vuimax": [
                Profile.DY.value,
            ],
            "vuimin": [
                Profile.DY.value,
            ],
            "tu1": [
                Profile.DY.value,
            ],
            "tu2": [
                Profile.DY.value,
            ],
            "tu3": [
                Profile.DY.value,
            ],
            "tu4": [
                Profile.DY.value,
            ],
            "vulmax": [
                Profile.DY.value,
            ],
            "vulmin": [
                Profile.DY.value,
            ],
        }
