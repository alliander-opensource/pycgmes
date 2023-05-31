"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass
class Pss5(PowerSystemStabilizerDynamics):
    """
    Detailed Italian PSS.

    kpe: Electric power input gain (KPE).  Typical value = 0,3.
    kf: Frequency/shaft speed input gain (KF).  Typical value = 5.
    isfreq: Selector for frequency/shaft speed input (isFreq). true = speed (same meaning as InputSignaKind.rotorSpeed)
      false = frequency (same meaning as InputSignalKind.busFrequency). Typical value = true (same meaning
      as InputSignalKind.rotorSpeed).
    kpss: PSS gain (KPSS).  Typical value = 1.
    ctw2: Selector for second washout enabling (CTW2). true = second washout filter is bypassed false = second washout
      filter in use. Typical value = true.
    tw1: First washout (TW1) (>= 0).  Typical value = 3,5.
    tw2: Second washout (TW2) (>= 0).  Typical value = 0.
    tl1: Lead/lag time constant (TL1) (>= 0).  Typical value = 0.
    tl2: Lead/lag time constant (TL2) (>= 0).  If = 0, both blocks are bypassed.  Typical value = 0.
    tl3: Lead/lag time constant (TL3) (>= 0).  Typical value = 0.
    tl4: Lead/lag time constant (TL4) (>= 0).  If = 0, both blocks are bypassed.  Typical value = 0.
    vsmn: Stabilizer output maximum limit (VSMN).  Typical value = -0,1.
    vsmx: Stabilizer output minimum limit (VSMX).  Typical value = 0,1.
    tpe: Electric power filter time constant (TPE) (>= 0).  Typical value = 0,05.
    pmin: Minimum power PSS enabling (Pmin).  Typical value = 0,25.
    deadband: Stabilizer output deadband (DEADBAND).  Typical value = 0.
    vadat: Signal selector (VadAtt). true = closed (generator power is greater than Pmin) false = open (Pe is smaller
      than Pmin). Typical value = true.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    kpe: float = 0.0  # Type #Float in CIM
    kf: float = 0.0  # Type #Float in CIM
    isfreq: bool = False  # Type #Boolean in CIM
    kpss: float = 0.0  # Type #Float in CIM
    ctw2: bool = False  # Type #Boolean in CIM
    tw1: int = 0  # Type #Seconds in CIM
    tw2: int = 0  # Type #Seconds in CIM
    tl1: int = 0  # Type #Seconds in CIM
    tl2: int = 0  # Type #Seconds in CIM
    tl3: int = 0  # Type #Seconds in CIM
    tl4: int = 0  # Type #Seconds in CIM
    vsmn: float = 0.0  # Type #PU in CIM
    vsmx: float = 0.0  # Type #PU in CIM
    tpe: int = 0  # Type #Seconds in CIM
    pmin: float = 0.0  # Type #PU in CIM
    deadband: float = 0.0  # Type #PU in CIM
    vadat: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=Pss5\n"
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
            "kpe": [
                self.profiles.DY.value,
            ],
            "kf": [
                self.profiles.DY.value,
            ],
            "isfreq": [
                self.profiles.DY.value,
            ],
            "kpss": [
                self.profiles.DY.value,
            ],
            "ctw2": [
                self.profiles.DY.value,
            ],
            "tw1": [
                self.profiles.DY.value,
            ],
            "tw2": [
                self.profiles.DY.value,
            ],
            "tl1": [
                self.profiles.DY.value,
            ],
            "tl2": [
                self.profiles.DY.value,
            ],
            "tl3": [
                self.profiles.DY.value,
            ],
            "tl4": [
                self.profiles.DY.value,
            ],
            "vsmn": [
                self.profiles.DY.value,
            ],
            "vsmx": [
                self.profiles.DY.value,
            ],
            "tpe": [
                self.profiles.DY.value,
            ],
            "pmin": [
                self.profiles.DY.value,
            ],
            "deadband": [
                self.profiles.DY.value,
            ],
            "vadat": [
                self.profiles.DY.value,
            ],
        }
