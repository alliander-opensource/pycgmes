"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics


@dataclass
class UnderexcLimX1(UnderexcitationLimiterDynamics):
    """
    Allis-Chalmers minimum excitation limiter.

    kf2: Differential gain (KF2).
    tf2: Differential time constant (TF2) (>= 0).
    km: Minimum excitation limit gain (KM).
    tm: Minimum excitation limit time constant (TM) (>= 0).
    melmax: Minimum excitation limit value (MELMAX).
    k: Minimum excitation limit slope (K) (> 0).
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    kf2: float = 0.0  # Type #PU in CIM
    tf2: int = 0  # Type #Seconds in CIM
    km: float = 0.0  # Type #PU in CIM
    tm: int = 0  # Type #Seconds in CIM
    melmax: float = 0.0  # Type #PU in CIM
    k: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=UnderexcLimX1\n"
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
            "kf2": [
                self.profiles.DY.value,
            ],
            "tf2": [
                self.profiles.DY.value,
            ],
            "km": [
                self.profiles.DY.value,
            ],
            "tm": [
                self.profiles.DY.value,
            ],
            "melmax": [
                self.profiles.DY.value,
            ],
            "k": [
                self.profiles.DY.value,
            ],
        }
