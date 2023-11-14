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
from .CrossCompoundTurbineGovernorDynamics import CrossCompoundTurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovSteamCC(CrossCompoundTurbineGovernorDynamics):
    """
    Cross compound turbine governor.  Unlike tandem compound units, cross compound units are not on the same shaft.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    pmaxhp: Maximum HP value position (Pmaxhp).  Typical value = 1.
    rhp: HP governor droop (Rhp) (> 0).  Typical value = 0,05.
    t1hp: HP governor time constant (T1hp) (>= 0).  Typical value = 0,1.
    t3hp: HP turbine time constant (T3hp) (>= 0).  Typical value = 0,1.
    t4hp: HP turbine time constant (T4hp) (>= 0).  Typical value = 0,1.
    t5hp: HP reheater time constant (T5hp) (>= 0).  Typical value = 10.
    fhp: Fraction of HP power ahead of reheater (Fhp).  Typical value = 0,3.
    dhp: HP damping factor (Dhp).  Typical value = 0.
    pmaxlp: Maximum LP value position (Pmaxlp).  Typical value = 1.
    rlp: LP governor droop (Rlp) (> 0).  Typical value = 0,05.
    t1lp: LP governor time constant (T1lp) (>= 0).  Typical value = 0,1.
    t3lp: LP turbine time constant (T3lp) (>= 0).  Typical value = 0,1.
    t4lp: LP turbine time constant (T4lp) (>= 0).  Typical value = 0,1.
    t5lp: LP reheater time constant (T5lp) (>= 0).  Typical value = 10.
    flp: Fraction of LP power ahead of reheater (Flp).  Typical value = 0,7.
    dlp: LP damping factor (Dlp).  Typical value = 0.
    """

    mwbase: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmaxhp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rhp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t1hp: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t3hp: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t4hp: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t5hp: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fhp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dhp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmaxlp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rlp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t1lp: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t3lp: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t4lp: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t5lp: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    flp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dlp: float = Field(
        default=0.0,
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
