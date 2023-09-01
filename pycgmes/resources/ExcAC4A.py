"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcAC4A(ExcitationSystemDynamics):
    """
    Modified IEEE AC4A alternator-supplied rectifier excitation system with different minimum controller output.

    vimax: Maximum voltage regulator input limit (Vimax)  (> 0).  Typical value = 10.
    vimin: Minimum voltage regulator input limit (Vimin) (< 0).  Typical value = -10.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 1.
    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 10.
    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 200.
    ta: Voltage regulator time constant (Ta) (> 0).  Typical value = 0,015.
    vrmax: Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 5,64.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -4,53.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 0.
    """

    vimax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vimin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tc: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tb: int = Field(
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

    kc: float = Field(
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
