"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcSCRX(ExcitationSystemDynamics):
    """
    Simple excitation system with generic characteristics typical of many excitation systems; intended for use where
      negative field current could be a problem.

    tatb: Gain reduction ratio of lag-lead element ([Ta / Tb]). The parameter Ta is not defined explicitly.  Typical
      value = 0.1.
    tb: Denominator time constant of lag-lead block (Tb) (>= 0).  Typical value = 10.
    k: Gain (K) (> 0).  Typical value = 200.
    te: Time constant of gain block (Te) (> 0).  Typical value = 0,02.
    emin: Minimum field voltage output (Emin) (< ExcSCRX.emax).  Typical value = 0.
    emax: Maximum field voltage output (Emax) (> ExcSCRX.emin).  Typical value = 5.
    cswitch: Power source switch (Cswitch). true = fixed voltage of 1.0 PU false = generator terminal voltage.
    rcrfd: Ratio of field discharge resistance to field winding resistance ([rc / rfd]).  Typical value = 0.
    """

    tatb: float = 0.0  # Type #Float in CIM
    tb: int = 0  # Type #Seconds in CIM
    k: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    emin: float = 0.0  # Type #PU in CIM
    emax: float = 0.0  # Type #PU in CIM
    cswitch: bool = False  # Type #Boolean in CIM
    rcrfd: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcSCRX"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "cswitch": [
                Profile.DY.value,
            ],
            "rcrfd": [
                Profile.DY.value,
            ],
        }
