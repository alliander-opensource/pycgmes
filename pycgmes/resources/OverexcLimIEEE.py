"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .OverexcitationLimiterDynamics import OverexcitationLimiterDynamics


@dataclass
class OverexcLimIEEE(OverexcitationLimiterDynamics):
    """
    The over excitation limiter model is intended to represent the significant features of OELs necessary for some
      large-scale system studies. It is the result of a pragmatic approach to obtain a model that can be widely
      applied with attainable data from generator owners. An attempt to include all variations in the functionality
      of OELs and duplicate how they interact with the rest of the excitation systems would likely result in a level
      of application insufficient for the studies for which they are intended. Reference: IEEE OEL 421.5-2005, 9.

    itfpu: OEL timed field current limiter pickup level (ITFPU).  Typical value = 1,05.
    ifdmax: OEL instantaneous field current limit (IFDMAX).  Typical value = 1,5.
    ifdlim: OEL timed field current limit (IFDLIM).  Typical value = 1,05.
    hyst: OEL pickup/drop-out hysteresis (HYST).  Typical value = 0,03.
    kcd: OEL cooldown gain (KCD).  Typical value = 1.
    kramp: OEL ramped limit rate (KRAMP).  Unit = PU / s.  Typical value = 10.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    itfpu: float = 0.0  # Type #PU in CIM
    ifdmax: float = 0.0  # Type #PU in CIM
    ifdlim: float = 0.0  # Type #PU in CIM
    hyst: float = 0.0  # Type #PU in CIM
    kcd: float = 0.0  # Type #PU in CIM
    kramp: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=OverexcLimIEEE\n"
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
            "itfpu": [
                self.profiles.DY.value,
            ],
            "ifdmax": [
                self.profiles.DY.value,
            ],
            "ifdlim": [
                self.profiles.DY.value,
            ],
            "hyst": [
                self.profiles.DY.value,
            ],
            "kcd": [
                self.profiles.DY.value,
            ],
            "kramp": [
                self.profiles.DY.value,
            ],
        }
