"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=PssIEEE1A\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.DY.value,
            ],
            # Attributes
            "inputSignalType": [
                self.profiles.DY.value,
            ],
            "a1": [
                self.profiles.DY.value,
            ],
            "a2": [
                self.profiles.DY.value,
            ],
            "t1": [
                self.profiles.DY.value,
            ],
            "t2": [
                self.profiles.DY.value,
            ],
            "t3": [
                self.profiles.DY.value,
            ],
            "t4": [
                self.profiles.DY.value,
            ],
            "t5": [
                self.profiles.DY.value,
            ],
            "t6": [
                self.profiles.DY.value,
            ],
            "ks": [
                self.profiles.DY.value,
            ],
            "vrmax": [
                self.profiles.DY.value,
            ],
            "vrmin": [
                self.profiles.DY.value,
            ],
        }
