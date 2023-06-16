"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass(config=DataclassConfig)
class PssSB4(PowerSystemStabilizerDynamics):
    """
    Power sensitive stabilizer model.

    tt: Time constant (Tt) (>= 0).  Typical value = 0,18.
    kx: Gain (Kx).  Typical value = 2,7.
    tx2: Time constant (Tx2) (>= 0).  Typical value = 5,0.
    ta: Time constant (Ta) (>= 0).  Typical value = 0,37.
    tx1: Reset time constant (Tx1) (>= 0).  Typical value = 0,035.
    tb: Time constant (Tb) (>= 0).  Typical value = 0,37.
    tc: Time constant (Tc) (>= 0).  Typical value = 0,035.
    td: Time constant (Td) (>= 0).  Typical value = 0,0.
    te: Time constant (Te) (>= 0).  Typical value = 0,0169.
    vsmax: Limiter (Vsmax) (> PssSB4.vsmin).  Typical value = 0,062.
    vsmin: Limiter (Vsmin) (< PssSB4.vsmax).  Typical value = -0,062.
    """

    tt: int = 0  # Type #Seconds in CIM
    kx: float = 0.0  # Type #PU in CIM
    tx2: int = 0  # Type #Seconds in CIM
    ta: int = 0  # Type #Seconds in CIM
    tx1: int = 0  # Type #Seconds in CIM
    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    td: int = 0  # Type #Seconds in CIM
    te: int = 0  # Type #Seconds in CIM
    vsmax: float = 0.0  # Type #PU in CIM
    vsmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PssSB4"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "tt": [
                Profile.DY.value,
            ],
            "kx": [
                Profile.DY.value,
            ],
            "tx2": [
                Profile.DY.value,
            ],
            "ta": [
                Profile.DY.value,
            ],
            "tx1": [
                Profile.DY.value,
            ],
            "tb": [
                Profile.DY.value,
            ],
            "tc": [
                Profile.DY.value,
            ],
            "td": [
                Profile.DY.value,
            ],
            "te": [
                Profile.DY.value,
            ],
            "vsmax": [
                Profile.DY.value,
            ],
            "vsmin": [
                Profile.DY.value,
            ],
        }
