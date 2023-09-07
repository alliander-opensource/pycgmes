# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovSteam0(TurbineGovernorDynamics):
    """
    A simplified steam turbine governor.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    r: Permanent droop (R).  Typical value = 0,05.
    t1: Steam bowl time constant (T1) (> 0).  Typical value = 0,5.
    vmax: Maximum valve position, PU of mwcap (Vmax) (> GovSteam0.vmin).  Typical value = 1.
    vmin: Minimum valve position, PU of mwcap (Vmin) (< GovSteam0.vmax).  Typical value = 0.
    t2: Numerator time constant of T2/T3 block (T2) (>= 0).  Typical value = 3.
    t3: Reheater time constant (T3) (> 0).  Typical value = 10.
    dt: Turbine damping coefficient (Dt).  Unit = delta P / delta speed. Typical value = 0.
    """

    mwbase: float = Field(
        default=0.0,
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

    t1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vmin: float = Field(
        default=0.0,
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

    t3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dt: float = Field(
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
