"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcNI(ExcitationSystemDynamics):
    """
    Bus or solid fed SCR (silicon-controlled rectifier) bridge excitation system model type NI (NVE).

    busFedSelector: Fed by selector (BusFedSelector).  true = bus fed (switch is closed) false = solid fed (switch is
      open). Typical value = true.
    tr: Time constant (Tr) (>= 0). Typical value = 0,02.
    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 210.
    ta: Voltage regulator time constant (Ta) (> 0).  Typical value = 0,02.
    vrmax: Maximum voltage regulator ouput (Vrmax) (> ExcNI.vrmin). Typical value = 5,0.
    vrmin: Minimum voltage regulator ouput (Vrmin) (< ExcNI.vrmax). Typical value = -2,0.
    kf: Excitation control system stabilizer gain (Kf) (> 0).  Typical value 0,01.
    tf2: Excitation control system stabilizer time constant (Tf2) (> 0). Typical value = 0,1.
    tf1: Excitation control system stabilizer time constant (Tf1) (> 0). Typical value = 1,0.
    r: rc / rfd (R) (>= 0).  0 means exciter has negative current capability > 0 means exciter does not have negative
      current capability.   Typical value = 5.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    busFedSelector: bool = False  # Type #Boolean in CIM
    tr: int = 0  # Type #Seconds in CIM
    ka: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    kf: float = 0.0  # Type #PU in CIM
    tf2: int = 0  # Type #Seconds in CIM
    tf1: int = 0  # Type #Seconds in CIM
    r: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcNI\n"
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
            "busFedSelector": [
                self.profiles.DY.value,
            ],
            "tr": [
                self.profiles.DY.value,
            ],
            "ka": [
                self.profiles.DY.value,
            ],
            "ta": [
                self.profiles.DY.value,
            ],
            "vrmax": [
                self.profiles.DY.value,
            ],
            "vrmin": [
                self.profiles.DY.value,
            ],
            "kf": [
                self.profiles.DY.value,
            ],
            "tf2": [
                self.profiles.DY.value,
            ],
            "tf1": [
                self.profiles.DY.value,
            ],
            "r": [
                self.profiles.DY.value,
            ],
        }
