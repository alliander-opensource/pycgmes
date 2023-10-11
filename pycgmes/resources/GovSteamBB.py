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
class GovSteamBB(TurbineGovernorDynamics):
    """
    European governor model.

    fcut: Frequency deadband (fcut) (>= 0).  Typical value = 0,002.
    ks: Gain (Ks).  Typical value = 21,0.
    kls: Gain (Kls) (> 0).  Typical value = 0,1.
    kg: Gain (Kg).  Typical value = 1,0.
    t1: Time constant (T1).  Typical value = 0,05.
    kp: Gain (Kp).  Typical value = 1,0.
    tn: Time constant (Tn) (> 0).  Typical value = 1,0.
    kd: Gain (Kd).  Typical value = 1,0.
    td: Time constant (Td) (> 0).  Typical value = 1,0.
    pmax: High power limit (Pmax) (> GovSteamBB.pmin).  Typical value = 1,0.
    pmin: Low power limit (Pmin) (< GovSteamBB.pmax).  Typical value = 0.
    t4: Time constant (T4).  Typical value = 0,15.
    k2: Gain (K2).  Typical value = 0,75.
    t5: Time constant (T5).  Typical value = 12,0.
    k3: Gain (K3).  Typical value = 0,5.
    t6: Time constant (T6).  Typical value = 0,75.
    peflag: Electric power input selection (Peflag).   true = electric power input false = feedback signal. Typical
      value = false.
    """

    fcut: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ks: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kls: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kg: float = Field(
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

    kp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tn: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kd: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    td: int = Field(
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

    t4: int = Field(
        default=0,
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

    t5: int = Field(
        default=0,
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

    t6: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    peflag: bool = Field(
        default=False,
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
