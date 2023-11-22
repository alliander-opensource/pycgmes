# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass
class PssPTIST1(PowerSystemStabilizerDynamics):
    """
    PTI microprocessor-based stabilizer type 1.

    m: (M).  M = 2 x H.  Typical value = 5.
    tf: Time constant (Tf) (>= 0).  Typical value = 0,2.
    tp: Time constant (Tp) (>= 0).  Typical value = 0,2.
    t1: Time constant (T1) (>= 0).  Typical value = 0,3.
    t2: Time constant (T2) (>= 0).  Typical value = 1.
    t3: Time constant (T3) (>= 0).  Typical value = 0,2.
    t4: Time constant (T4) (>= 0).  Typical value = 0,05.
    k: Gain (K).  Typical value = 9.
    dtf: Time step frequency calculation (deltatf) (>= 0).  Typical value = 0,025.
    dtc: Time step related to activation of controls (deltatc) (>= 0).  Typical value = 0,025.
    dtp: Time step active power calculation (deltatp) (>= 0).  Typical value = 0,0125.
    """

    m: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tf: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tp: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t1: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t2: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t3: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t4: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    k: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    dtf: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    dtc: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    dtp: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
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
