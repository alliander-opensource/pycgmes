# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovSteamSGO(TurbineGovernorDynamics):
    """
    Simplified steam turbine governor.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    t1: Controller lag (T1) (>= 0).
    t2: Controller lead compensation (T2) (>= 0).
    t3: Governor lag (T3) (> 0).
    t4: Delay due to steam inlet volumes associated with steam chest and inlet piping (T4) (>= 0).
    t5: Reheater delay including hot and cold leads (T5) (>= 0).
    t6: Delay due to IP-LP turbine, crossover pipes and LP end hoods (T6) (>= 0).
    k1: One / PU regulation (K1).
    k2: Fraction (K2).
    k3: Fraction (K3).
    pmax: Upper power limit (Pmax) (> GovSteamSGO.pmin).
    pmin: Lower power limit (Pmin) (>= 0 and < GovSteamSGO.pmax).
    """

    mwbase: float = Field(
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

    t3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t4: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t5: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t6: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k3: float = Field(
        default=0.0,
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

    pmin: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
