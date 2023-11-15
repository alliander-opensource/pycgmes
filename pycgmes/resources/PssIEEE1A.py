# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass
class PssIEEE1A(PowerSystemStabilizerDynamics):
    """
    IEEE 421.5-2005 type PSS1A power system stabilizer model. PSS1A is the generalized form of a PSS with a single input
      signal.  Reference: IEEE 1A 421.5-2005, 8.1.

    inputSignalType: Type of input signal (rotorAngularFrequencyDeviation, generatorElectricalPower, or
      busFrequencyDeviation).  Typical value = rotorAngularFrequencyDeviation.
    a1: PSS signal conditioning frequency filter constant (A1).  Typical value = 0,061.
    a2: PSS signal conditioning frequency filter constant (A2).  Typical value = 0,0017.
    t1: Lead/lag time constant (T1) (>= 0).  Typical value = 0,3.
    t2: Lead/lag time constant (T2) (>= 0).  Typical value = 0,03.
    t3: Lead/lag time constant (T3) (>= 0).  Typical value = 0,3.
    t4: Lead/lag time constant (T4) (>= 0).  Typical value = 0,03.
    t5: Washout time constant (T5) (>= 0).  Typical value = 10.
    t6: Transducer time constant (T6) (>= 0).  Typical value = 0,01.
    ks: Stabilizer gain (Ks).  Typical value = 5.
    vrmax: Maximum stabilizer output (Vrmax) (> PssIEEE1A.vrmin).  Typical value = 0,05.
    vrmin: Minimum stabilizer output (Vrmin) (< PssIEEE1A.vrmax).  Typical value = -0,05.
    """

    inputSignalType: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    a1: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    a2: float = Field(
        default=0.0,
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

    t5: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t6: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ks: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    vrmax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    vrmin: float = Field(
        default=0.0,
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
