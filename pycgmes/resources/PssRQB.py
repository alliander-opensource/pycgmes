"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass(config=DataclassConfig)
class PssRQB(PowerSystemStabilizerDynamics):
    """
    Power system stabilizer type RQB. This power system stabilizer is intended to be used together with excitation
      system type ExcRQB, which is primarily used in nuclear or thermal generating units.

    ki2: Speed input gain (Ki2). Typical value = 3,43.
    ki3: Electrical power input gain (Ki3). Typical value = -11,45.
    ki4: Mechanical power input gain (Ki4). Typical value = 11,86.
    t4m: Input time constant (T4M) (>= 0). Typical value = 5.
    tomd: Speed delay (TOMD) (>= 0). Typical value = 0,02.
    tomsl: Speed time constant (TOMSL) (>= 0). Typical value = 0,04.
    t4mom: Speed time constant (T4MOM) (>= 0). Typical value = 1,27.
    sibv: Speed deadband (SIBV). Typical value = 0,006.
    kdpm: Lead lag gain (KDPM). Typical value = 0,185.
    t4f: Lead lag time constant (T4F) (>= 0). Typical value = 0,045.
    """

    ki2: float = 0.0  # Type #Float in CIM
    ki3: float = 0.0  # Type #Float in CIM
    ki4: float = 0.0  # Type #Float in CIM
    t4m: int = 0  # Type #Seconds in CIM
    tomd: int = 0  # Type #Seconds in CIM
    tomsl: int = 0  # Type #Seconds in CIM
    t4mom: int = 0  # Type #Seconds in CIM
    sibv: float = 0.0  # Type #PU in CIM
    kdpm: float = 0.0  # Type #Float in CIM
    t4f: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PssRQB"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "ki2": [
                Profile.DY.value,
            ],
            "ki3": [
                Profile.DY.value,
            ],
            "ki4": [
                Profile.DY.value,
            ],
            "t4m": [
                Profile.DY.value,
            ],
            "tomd": [
                Profile.DY.value,
            ],
            "tomsl": [
                Profile.DY.value,
            ],
            "t4mom": [
                Profile.DY.value,
            ],
            "sibv": [
                Profile.DY.value,
            ],
            "kdpm": [
                Profile.DY.value,
            ],
            "t4f": [
                Profile.DY.value,
            ],
        }
