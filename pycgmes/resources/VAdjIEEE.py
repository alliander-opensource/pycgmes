"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .VoltageAdjusterDynamics import VoltageAdjusterDynamics


@dataclass(config=DataclassConfig)
class VAdjIEEE(VoltageAdjusterDynamics):
    """
    IEEE voltage adjuster which is used to represent the voltage adjuster in either a power factor or VAr control
      system. Reference: IEEE 421.5-2005, 11.1.

    vadjf: Set high to provide a continuous raise or lower (VADJF).
    adjslew: Rate at which output of adjuster changes (ADJ_SLEW).  Unit = s / PU.  Typical value = 300.
    vadjmax: Maximum output of the adjuster (VADJMAX) (> VAdjIEEE.vadjmin).  Typical value = 1,1.
    vadjmin: Minimum output of the adjuster (VADJMIN) (< VAdjIEEE.vadjmax).  Typical value = 0,9.
    taon: Time that adjuster pulses are on (TAON) (>= 0).  Typical value = 0,1.
    taoff: Time that adjuster pulses are off (TAOFF) (>= 0).  Typical value = 0,5.
    """

    vadjf: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    adjslew: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vadjmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vadjmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    taon: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    taoff: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
