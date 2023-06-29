"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovSteam2(TurbineGovernorDynamics):
    """
    Simplified governor.

    k: Governor gain (reciprocal of droop) (K).  Typical value = 20.
    dbf: Frequency deadband (DBF).  Typical value = 0.
    t1: Governor lag time constant (T1) (> 0).  Typical value = 0,45.
    t2: Governor lead time constant (T2) (>= 0).  Typical value = 0.
    pmax: Maximum fuel flow (PMAX) (> GovSteam2.pmin).  Typical value = 1.
    pmin: Minimum fuel flow (PMIN) (< GovSteam2.pmax).  Typical value = 0.
    mxef: Fuel flow maximum positive error value (MXEF).  Typical value = 1.
    mnef: Fuel flow maximum negative error value (MNEF).  Typical value = -1.
    """

    k: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dbf: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    mxef: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    mnef: float = Field(
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
