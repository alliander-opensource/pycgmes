"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass(config=DataclassConfig)
class PssIEEE1A(PowerSystemStabilizerDynamics):
    """
    IEEE 421.5-2005 type PSS1A power system stabilizer model. PSS1A is the generalized form of a PSS with a single input
      signal.  Reference: IEEE 1A 421.5-2005, 8.1.

    inputSignalType: Type of input signal (rotorAngularFrequencyDeviation, generatorElectricalPower, or
      busFrequencyDeviation).  Typical value = rotorAngularFrequencyDeviation.
    a1: PSS signal conditioning frequency filter constant (A1).  Typical value = 0,061.
    a2: PSS signal conditioning frequency filter constant (A2).  Typical value = 0,0017.
    t1: Lead/lag time constant (T1) (>= 0).  Typical value = 0,3.
    t2: Lead/lag time constant (T2) (>= 0).  Typical value = 0,03.
    t3: Lead/lag time constant (T3) (>= 0).  Typical value = 0,3.
    t4: Lead/lag time constant (T4) (>= 0).  Typical value = 0,03.
    t5: Washout time constant (T5) (>= 0).  Typical value = 10.
    t6: Transducer time constant (T6) (>= 0).  Typical value = 0,01.
    ks: Stabilizer gain (Ks).  Typical value = 5.
    vrmax: Maximum stabilizer output (Vrmax) (> PssIEEE1A.vrmin).  Typical value = 0,05.
    vrmin: Minimum stabilizer output (Vrmin) (< PssIEEE1A.vrmax).  Typical value = -0,05.
    """

    inputSignalType: Optional[str] = None  # Type M:1..1 in CIM
    a1: float = 0.0  # Type #PU in CIM
    a2: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    t5: int = 0  # Type #Seconds in CIM
    t6: int = 0  # Type #Seconds in CIM
    ks: float = 0.0  # Type #PU in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PssIEEE1A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "inputSignalType": [
                Profile.DY.value,
            ],
            "a1": [
                Profile.DY.value,
            ],
            "a2": [
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
            "ks": [
                Profile.DY.value,
            ],
            "vrmax": [
                Profile.DY.value,
            ],
            "vrmin": [
                Profile.DY.value,
            ],
        }
