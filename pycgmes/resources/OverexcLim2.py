"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .OverexcitationLimiterDynamics import OverexcitationLimiterDynamics


@dataclass
class OverexcLim2(OverexcitationLimiterDynamics):
    """
    Different from LimIEEEOEL, LimOEL2 has a fixed pickup threshold and reduces the excitation set-point by means of a
      non-windup integral regulator. Irated is the rated machine excitation current (calculated from nameplate
      conditions: Vnom, Pnom, CosPhinom).

    koi: Gain Over excitation limiter (KOI).  Typical value = 0,1.
    voimax: Maximum error signal (VOIMAX) (> OverexcLim2.voimin).  Typical value = 0.
    voimin: Minimum error signal (VOIMIN) (< OverexcLim2.voimax).  Typical value = -9999.
    ifdlim: Limit value of rated field current (IFDLIM).  Typical value = 1,05.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    koi: float = 0.0  # Type #PU in CIM
    voimax: float = 0.0  # Type #PU in CIM
    voimin: float = 0.0  # Type #PU in CIM
    ifdlim: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=OverexcLim2\n"
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
            "koi": [
                self.profiles.DY.value,
            ],
            "voimax": [
                self.profiles.DY.value,
            ],
            "voimin": [
                self.profiles.DY.value,
            ],
            "ifdlim": [
                self.profiles.DY.value,
            ],
        }
