"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass
class PssIEEE3B(PowerSystemStabilizerDynamics):
    """
    IEEE 421.5-2005 type PSS3B power system stabilizer model. The PSS model PSS3B has dual inputs of electrical power
      and rotor angular frequency deviation. The signals are used to derive an equivalent mechanical power signal.
      This model has 2 input signals. They have the following fixed types (expressed in terms of InputSignalKind
      values): the first one is of rotorAngleFrequencyDeviation type and the second one is of
      generatorElectricalPower type. Reference: IEEE 3B 421.5-2005, 8.3.

    t1: Transducer time constant (T1) (>= 0).  Typical value = 0,012.
    t2: Transducer time constant (T2) (>= 0).  Typical value = 0,012.
    tw1: Washout time constant (Tw1) (>= 0).  Typical value = 0,3.
    tw2: Washout time constant (Tw2) (>= 0).  Typical value = 0,3.
    tw3: Washout time constant (Tw3) (>= 0).  Typical value = 0,6.
    ks1: Gain on signal # 1 (Ks1).  Typical value = -0,602.
    ks2: Gain on signal # 2 (Ks2).  Typical value = 30,12.
    a1: Notch filter parameter (A1).  Typical value = 0,359.
    a2: Notch filter parameter (A2).  Typical value = 0,586.
    a3: Notch filter parameter (A3).  Typical value = 0,429.
    a4: Notch filter parameter (A4).  Typical value = 0,564.
    a5: Notch filter parameter (A5).  Typical value = 0,001.
    a6: Notch filter parameter (A6).  Typical value = 0.
    a7: Notch filter parameter (A7).  Typical value = 0,031.
    a8: Notch filter parameter (A8).  Typical value = 0.
    vstmax: Stabilizer output maximum limit (Vstmax) (> PssIEEE3B.vstmin).  Typical value = 0,1.
    vstmin: Stabilizer output minimum limit (Vstmin) (< PssIEEE3B.vstmax).  Typical value = -0,1.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    tw1: int = 0  # Type #Seconds in CIM
    tw2: int = 0  # Type #Seconds in CIM
    tw3: int = 0  # Type #Seconds in CIM
    ks1: float = 0.0  # Type #PU in CIM
    ks2: float = 0.0  # Type #PU in CIM
    a1: float = 0.0  # Type #PU in CIM
    a2: float = 0.0  # Type #PU in CIM
    a3: float = 0.0  # Type #PU in CIM
    a4: float = 0.0  # Type #PU in CIM
    a5: float = 0.0  # Type #PU in CIM
    a6: float = 0.0  # Type #PU in CIM
    a7: float = 0.0  # Type #PU in CIM
    a8: float = 0.0  # Type #PU in CIM
    vstmax: float = 0.0  # Type #PU in CIM
    vstmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PssIEEE3B\n"
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
            "t1": [
                self.profiles.DY.value,
            ],
            "t2": [
                self.profiles.DY.value,
            ],
            "tw1": [
                self.profiles.DY.value,
            ],
            "tw2": [
                self.profiles.DY.value,
            ],
            "tw3": [
                self.profiles.DY.value,
            ],
            "ks1": [
                self.profiles.DY.value,
            ],
            "ks2": [
                self.profiles.DY.value,
            ],
            "a1": [
                self.profiles.DY.value,
            ],
            "a2": [
                self.profiles.DY.value,
            ],
            "a3": [
                self.profiles.DY.value,
            ],
            "a4": [
                self.profiles.DY.value,
            ],
            "a5": [
                self.profiles.DY.value,
            ],
            "a6": [
                self.profiles.DY.value,
            ],
            "a7": [
                self.profiles.DY.value,
            ],
            "a8": [
                self.profiles.DY.value,
            ],
            "vstmax": [
                self.profiles.DY.value,
            ],
            "vstmin": [
                self.profiles.DY.value,
            ],
        }
