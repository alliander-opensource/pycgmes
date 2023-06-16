"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcSEXS(ExcitationSystemDynamics):
    """
    Simplified excitation system.

    tatb: Gain reduction ratio of lag-lead element ([Ta / Tb]).  Typical value = 0,1.
    tb: Denominator time constant of lag-lead block (Tb) (>= 0).  Typical value = 10.
    k: Gain (K) (> 0).  Typical value = 100.
    te: Time constant of gain block (Te) (> 0).  Typical value = 0,05.
    emin: Minimum field voltage output (Emin) (< ExcSEXS.emax).  Typical value = -5.
    emax: Maximum field voltage output (Emax) (> ExcSEXS.emin).  Typical value = 5.
    kc: PI controller gain (Kc) (> 0 if ExcSEXS.tc > 0).  Typical value = 0,08.
    tc: PI controller phase lead time constant (Tc) (>= 0).  Typical value = 0.
    efdmin: Field voltage clipping minimum limit (Efdmin) (< ExcSEXS.efdmax).  Typical value = -5.
    efdmax: Field voltage clipping maximum limit (Efdmax) (> ExcSEXS.efdmin).  Typical value = 5.
    """

    tatb: float = 0.0  # Type #Float in CIM
    tb: int = 0  # Type #Seconds in CIM
    k: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    emin: float = 0.0  # Type #PU in CIM
    emax: float = 0.0  # Type #PU in CIM
    kc: float = 0.0  # Type #PU in CIM
    tc: int = 0  # Type #Seconds in CIM
    efdmin: float = 0.0  # Type #PU in CIM
    efdmax: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcSEXS"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "tatb": [
                Profile.DY.value,
            ],
            "tb": [
                Profile.DY.value,
            ],
            "k": [
                Profile.DY.value,
            ],
            "te": [
                Profile.DY.value,
            ],
            "emin": [
                Profile.DY.value,
            ],
            "emax": [
                Profile.DY.value,
            ],
            "kc": [
                Profile.DY.value,
            ],
            "tc": [
                Profile.DY.value,
            ],
            "efdmin": [
                Profile.DY.value,
            ],
            "efdmax": [
                Profile.DY.value,
            ],
        }
