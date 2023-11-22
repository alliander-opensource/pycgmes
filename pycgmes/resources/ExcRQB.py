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
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcRQB(ExcitationSystemDynamics):
    """
    Excitation system type RQB (four-loop regulator, r?gulateur quatre boucles, developed in France) primarily used in
      nuclear or thermal generating units. This excitation system shall be always used together with power system
      stabilizer type PssRQB.

    ki0: Voltage reference input gain (Ki0).  Typical value = 12,7.
    ki1: Voltage input gain (Ki1).  Typical value = -16,8.
    te: Lead lag time constant (TE) (>= 0).  Typical value = 0,22.
    tc: Lead lag time constant (TC) (>= 0).  Typical value = 0,02.
    klir: OEL input gain (KLIR).  Typical value = 12,13.
    ucmin: Minimum voltage reference limit (UCMIN) (< ExcRQB.ucmax).  Typical value = 0,9.
    ucmax: Maximum voltage reference limit (UCMAX) (> ExcRQB.ucmin).  Typical value = 1,1.
    lus: Setpoint (LUS).  Typical value = 0,12.
    klus: Limiter gain (KLUS).  Typical value = 50.
    mesu: Voltage input time constant (MESU) (>= 0).  Typical value = 0,02.
    t4m: Input time constant (T4M) (>= 0).  Typical value = 5.
    lsat: Integrator limiter (LSAT).  Typical value = 5,73.
    tf: Exciter time constant (TF) (>= 0).  Typical value = 0,01.
    """

    ki0: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ki1: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    te: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tc: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    klir: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ucmin: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ucmax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    lus: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    klus: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    mesu: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t4m: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    lsat: float = Field(
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

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
