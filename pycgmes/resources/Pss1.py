"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass
class Pss1(PowerSystemStabilizerDynamics):
    """
    Italian PSS with three inputs (speed, frequency, power).

    komega: Shaft speed power input gain (Komega).  Typical value = 0.
    kf: Frequency power input gain (KF).  Typical value = 5.
    kpe: Electric power input gain (KPE).  Typical value = 0,3.
    pmin: Minimum power PSS enabling (Pmin).  Typical value = 0,25.
    ks: PSS gain (Ks).  Typical value = 1.
    vsmn: Stabilizer output maximum limit (VSMN).  Typical value = -0,06.
    vsmx: Stabilizer output minimum limit (VSMX).  Typical value = 0,06.
    tpe: Electric power filter time constant (TPE) (>= 0).  Typical value = 0,05.
    t5: Washout (T5) (>= 0).  Typical value = 3,5.
    t6: Filter time constant (T6) (>= 0).  Typical value = 0.
    t7: Lead/lag time constant (T7) (>= 0). If = 0, both blocks are bypassed.  Typical value = 0.
    t8: Lead/lag time constant (T8) (>= 0).  Typical value = 0.
    t9: Lead/lag time constant (T9) (>= 0).  If = 0, both blocks are bypassed.  Typical value = 0.
    t10: Lead/lag time constant (T10) (>= 0).  Typical value = 0.
    vadat: Signal selector (VADAT). true = closed (generator power is greater than Pmin) false = open (Pe is smaller
      than Pmin). Typical value = true.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    komega: float = 0.0  # Type #Float in CIM
    kf: float = 0.0  # Type #Float in CIM
    kpe: float = 0.0  # Type #Float in CIM
    pmin: float = 0.0  # Type #PU in CIM
    ks: float = 0.0  # Type #Float in CIM
    vsmn: float = 0.0  # Type #PU in CIM
    vsmx: float = 0.0  # Type #PU in CIM
    tpe: int = 0  # Type #Seconds in CIM
    t5: int = 0  # Type #Seconds in CIM
    t6: int = 0  # Type #Seconds in CIM
    t7: int = 0  # Type #Seconds in CIM
    t8: int = 0  # Type #Seconds in CIM
    t9: int = 0  # Type #Seconds in CIM
    t10: int = 0  # Type #Seconds in CIM
    vadat: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=Pss1\n"
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
            "komega": [
                self.profiles.DY.value,
            ],
            "kf": [
                self.profiles.DY.value,
            ],
            "kpe": [
                self.profiles.DY.value,
            ],
            "pmin": [
                self.profiles.DY.value,
            ],
            "ks": [
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
            "t5": [
                self.profiles.DY.value,
            ],
            "t6": [
                self.profiles.DY.value,
            ],
            "t7": [
                self.profiles.DY.value,
            ],
            "t8": [
                self.profiles.DY.value,
            ],
            "t9": [
                self.profiles.DY.value,
            ],
            "t10": [
                self.profiles.DY.value,
            ],
            "vadat": [
                self.profiles.DY.value,
            ],
        }
