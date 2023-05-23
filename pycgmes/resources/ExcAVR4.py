"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcAVR4(ExcitationSystemDynamics):
    """
    Italian excitation system. It represents a static exciter and electric voltage regulator.

    ka: AVR gain (KA).  Typical value = 300.
    vrmn: Minimum AVR output (VRMN).  Typical value = 0.
    vrmx: Maximum AVR output (VRMX).  Typical value = 5.
    t1: AVR time constant (T1) (>= 0).  Typical value = 4,8.
    t2: AVR time constant (T2) (>= 0).  Typical value = 1,5.
    t3: AVR time constant (T3) (>= 0).  Typical value = 0.
    t4: AVR time constant (T4) (>= 0).  Typical value = 0.
    ke: Exciter gain (KE).  Typical value = 1.
    vfmx: Maximum exciter output (VFMX).  Typical value = 5.
    vfmn: Minimum exciter output (VFMN).  Typical value = 0.
    kif: Exciter internal reactance (KIF).  Typical value = 0.
    tif: Exciter current feedback time constant (TIF) (>= 0).  Typical value = 0.
    t1if: Exciter current feedback time constant (T1IF) (>= 0).  Typical value = 60.
    imul: AVR output voltage dependency selector (IMUL). true = selector is connected false = selector is not connected.
      Typical value = true.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ka: float = 0.0  # Type #Float in CIM
    vrmn: float = 0.0  # Type #PU in CIM
    vrmx: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    ke: float = 0.0  # Type #Float in CIM
    vfmx: float = 0.0  # Type #PU in CIM
    vfmn: float = 0.0  # Type #PU in CIM
    kif: float = 0.0  # Type #Float in CIM
    tif: int = 0  # Type #Seconds in CIM
    t1if: int = 0  # Type #Seconds in CIM
    imul: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcAVR4\n"
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
            "ka": [
                self.profiles.DY.value,
            ],
            "vrmn": [
                self.profiles.DY.value,
            ],
            "vrmx": [
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
            "ke": [
                self.profiles.DY.value,
            ],
            "vfmx": [
                self.profiles.DY.value,
            ],
            "vfmn": [
                self.profiles.DY.value,
            ],
            "kif": [
                self.profiles.DY.value,
            ],
            "tif": [
                self.profiles.DY.value,
            ],
            "t1if": [
                self.profiles.DY.value,
            ],
            "imul": [
                self.profiles.DY.value,
            ],
        }
