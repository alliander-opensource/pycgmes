"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .OverexcitationLimiterDynamics import OverexcitationLimiterDynamics


@dataclass
class OverexcLimX2(OverexcitationLimiterDynamics):
    """
    Field voltage or current overexcitation limiter designed to protect the generator field of an AC machine with
      automatic excitation control from overheating due to prolonged overexcitation.

    m: (m). true = IFD limiting false = EFD limiting.
    efdrated: Rated field voltage if m = false or rated field current if m = true (EFDRATED).  Typical value = 1,05.
    efd1: Low voltage or current point on the inverse time characteristic (EFD1).  Typical value = 1,1.
    t1: Time to trip the exciter at the low voltage or current point on the inverse time characteristic (TIME1) (>= 0).
      Typical value = 120.
    efd2: Mid voltage or current point on the inverse time characteristic (EFD2).  Typical value = 1,2.
    t2: Time to trip the exciter at the mid voltage or current point on the inverse time characteristic (TIME2) (>= 0).
      Typical value = 40.
    efd3: High voltage or current point on the inverse time characteristic (EFD3).  Typical value = 1,5.
    t3: Time to trip the exciter at the high voltage or current point on the inverse time characteristic (TIME3) (>= 0).
      Typical value = 15.
    efddes: Desired field voltage if m = false or desired field current if m = true (EFDDES).  Typical value = 1.
    kmx: Gain (KMX).  Typical value = 0,002.
    vlow: Low voltage limit (VLOW) (> 0).
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    m: bool = False  # Type #Boolean in CIM
    efdrated: float = 0.0  # Type #PU in CIM
    efd1: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    efd2: float = 0.0  # Type #PU in CIM
    t2: int = 0  # Type #Seconds in CIM
    efd3: float = 0.0  # Type #PU in CIM
    t3: int = 0  # Type #Seconds in CIM
    efddes: float = 0.0  # Type #PU in CIM
    kmx: float = 0.0  # Type #PU in CIM
    vlow: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=OverexcLimX2\n"
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
            "m": [
                self.profiles.DY.value,
            ],
            "efdrated": [
                self.profiles.DY.value,
            ],
            "efd1": [
                self.profiles.DY.value,
            ],
            "t1": [
                self.profiles.DY.value,
            ],
            "efd2": [
                self.profiles.DY.value,
            ],
            "t2": [
                self.profiles.DY.value,
            ],
            "efd3": [
                self.profiles.DY.value,
            ],
            "t3": [
                self.profiles.DY.value,
            ],
            "efddes": [
                self.profiles.DY.value,
            ],
            "kmx": [
                self.profiles.DY.value,
            ],
            "vlow": [
                self.profiles.DY.value,
            ],
        }
