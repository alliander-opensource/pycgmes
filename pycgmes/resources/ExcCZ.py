"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcCZ(ExcitationSystemDynamics):
    """
    Czech proportion/integral exciter.

    kp: Regulator proportional gain (Kp).
    tc: Regulator integral time constant (Tc) (>= 0).
    vrmax: Voltage regulator maximum limit (Vrmax) (> ExcCZ.vrmin).
    vrmin: Voltage regulator minimum limit (Vrmin) (< ExcCZ.vrmax).
    ka: Regulator gain (Ka).
    ta: Regulator time constant (Ta) (>= 0).
    ke: Exciter constant related to self-excited field (Ke).
    te: Exciter time constant, integration rate associated with exciter control (Te) (>= 0).
    efdmax: Exciter output maximum limit (Efdmax) (> ExcCZ.efdmin).
    efdmin: Exciter output minimum limit (Efdmin) (< ExcCZ.efdmax).
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    kp: float = 0.0  # Type #PU in CIM
    tc: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    ka: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    ke: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    efdmax: float = 0.0  # Type #PU in CIM
    efdmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcCZ\n"
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
            "kp": [
                self.profiles.DY.value,
            ],
            "tc": [
                self.profiles.DY.value,
            ],
            "vrmax": [
                self.profiles.DY.value,
            ],
            "vrmin": [
                self.profiles.DY.value,
            ],
            "ka": [
                self.profiles.DY.value,
            ],
            "ta": [
                self.profiles.DY.value,
            ],
            "ke": [
                self.profiles.DY.value,
            ],
            "te": [
                self.profiles.DY.value,
            ],
            "efdmax": [
                self.profiles.DY.value,
            ],
            "efdmin": [
                self.profiles.DY.value,
            ],
        }
