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
from .ConductingEquipment import ConductingEquipment


@dataclass
class SeriesCompensator(ConductingEquipment):
    """
    A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.  It
      is a two terminal device.

    r: Positive sequence resistance.
    x: Positive sequence reactance.
    r0: Zero sequence resistance.
    x0: Zero sequence reactance.
    varistorPresent: Describe if a metal oxide varistor (mov) for over voltage protection is configured in parallel with
      the series compensator. It is used for short circuit calculations.
    varistorRatedCurrent: The maximum current the varistor is designed to handle at specified duration. It is used for
      short circuit calculations and exchanged only if SeriesCompensator.varistorPresent is
      true. The attribute shall be a positive value.
    varistorVoltageThreshold: The dc voltage at which the varistor starts conducting. It is used for short circuit
      calculations and exchanged only if SeriesCompensator.varistorPresent is true.
    """

    r: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
    )

    x: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
    )

    r0: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ]
        },
    )

    x0: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ]
        },
    )

    varistorPresent: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ]
        },
    )

    varistorRatedCurrent: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ]
        },
    )

    varistorVoltageThreshold: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
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
            Profile.EQ,
            Profile.SC,
        }
