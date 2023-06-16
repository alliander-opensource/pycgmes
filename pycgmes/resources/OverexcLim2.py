"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .OverexcitationLimiterDynamics import OverexcitationLimiterDynamics


@dataclass(config=DataclassConfig)
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

    koi: float = 0.0  # Type #PU in CIM
    voimax: float = 0.0  # Type #PU in CIM
    voimin: float = 0.0  # Type #PU in CIM
    ifdlim: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=OverexcLim2"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "koi": [
                Profile.DY.value,
            ],
            "voimax": [
                Profile.DY.value,
            ],
            "voimin": [
                Profile.DY.value,
            ],
            "ifdlim": [
                Profile.DY.value,
            ],
        }
