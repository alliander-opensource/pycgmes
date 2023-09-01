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
class GovHydro1(TurbineGovernorDynamics):
    """
    Basic hydro turbine governor.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    rperm: Permanent droop (R) (> 0).  Typical value = 0,04.
    rtemp: Temporary droop (r) (> GovHydro1.rperm).  Typical value = 0,3.
    tr: Washout time constant (Tr) (> 0).  Typical value = 5.
    tf: Filter time constant (Tf) (> 0).  Typical value = 0,05.
    tg: Gate servo time constant (Tg) (> 0).  Typical value = 0,5.
    velm: Maximum gate velocity (Vlem) (> 0).  Typical value = 0,2.
    gmax: Maximum gate opening (Gmax) (> 0 and > GovHydro.gmin).  Typical value = 1.
    gmin: Minimum gate opening (Gmin) (>= 0 and < GovHydro1.gmax).  Typical value = 0.
    tw: Water inertia time constant (Tw) (> 0).  Typical value = 1.
    at: Turbine gain (At) (> 0).  Typical value = 1,2.
    dturb: Turbine damping factor (Dturb) (>= 0).  Typical value = 0,5.
    qnl: No-load flow at nominal head (qnl) (>= 0).  Typical value = 0,08.
    hdam: Turbine nominal head (hdam).  Typical value = 1.
    """

    mwbase: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rperm: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rtemp: float = Field(
        default=0.0,
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

    tf: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tg: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    velm: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tw: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    at: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dturb: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    qnl: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    hdam: float = Field(
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
