"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .OverexcitationLimiterDynamics import OverexcitationLimiterDynamics


@dataclass(config=DataclassConfig)
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

    itfpu: float = 0.0  # Type #PU in CIM
    ifdmax: float = 0.0  # Type #PU in CIM
    ifdlim: float = 0.0  # Type #PU in CIM
    hyst: float = 0.0  # Type #PU in CIM
    kcd: float = 0.0  # Type #PU in CIM
    kramp: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=OverexcLimIEEE"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.DY.value,
            ],
            # Attributes
            "itfpu": [
                Profile.DY.value,
            ],
            "ifdmax": [
                Profile.DY.value,
            ],
            "ifdlim": [
                Profile.DY.value,
            ],
            "hyst": [
                Profile.DY.value,
            ],
            "kcd": [
                Profile.DY.value,
            ],
            "kramp": [
                Profile.DY.value,
            ],
        }
