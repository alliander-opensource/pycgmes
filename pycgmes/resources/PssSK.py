"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass(config=DataclassConfig)
class PssSK(PowerSystemStabilizerDynamics):
    """
    Slovakian PSS with three inputs.

    k1: Gain P (K1).  Typical value = -0,3.
    k2: Gain fE (K2).  Typical value = -0,15.
    k3: Gain If (K3).  Typical value = 10.
    t1: Denominator time constant (T1) (> 0,005).  Typical value = 0,3.
    t2: Filter time constant (T2) (> 0,005).  Typical value = 0,35.
    t3: Denominator time constant (T3) (> 0,005).  Typical value = 0,22.
    t4: Filter time constant (T4) (> 0,005).  Typical value = 0,02.
    t5: Denominator time constant (T5) (> 0,005).  Typical value = 0,02.
    t6: Filter time constant (T6) (> 0,005).  Typical value = 0,02.
    vsmax: Stabilizer output maximum limit (VSMAX) (> PssSK.vsmin).  Typical value = 0,4.
    vsmin: Stabilizer output minimum limit (VSMIN) (< PssSK.vsmax).  Typical value = -0.4.
    """

    k1: float = 0.0  # Type #PU in CIM
    k2: float = 0.0  # Type #PU in CIM
    k3: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    t5: int = 0  # Type #Seconds in CIM
    t6: int = 0  # Type #Seconds in CIM
    vsmax: float = 0.0  # Type #PU in CIM
    vsmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PssSK"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "k1": [
                Profile.DY.value,
            ],
            "k2": [
                Profile.DY.value,
            ],
            "k3": [
                Profile.DY.value,
            ],
            "t1": [
                Profile.DY.value,
            ],
            "t2": [
                Profile.DY.value,
            ],
            "t3": [
                Profile.DY.value,
            ],
            "t4": [
                Profile.DY.value,
            ],
            "t5": [
                Profile.DY.value,
            ],
            "t6": [
                Profile.DY.value,
            ],
            "vsmax": [
                Profile.DY.value,
            ],
            "vsmin": [
                Profile.DY.value,
            ],
        }
