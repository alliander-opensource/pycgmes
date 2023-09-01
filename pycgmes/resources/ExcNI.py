"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
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

    busFedSelector: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    tr: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ka: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ta: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vrmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vrmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kf: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tf2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tf1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    r: float = Field(
        default=0.0,
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
