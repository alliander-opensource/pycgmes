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
from .IdentifiedObject import IdentifiedObject


@dataclass
class Season(IdentifiedObject):
    """
    A specified time period of the year.

    endDate: Date season ends.
    startDate: Date season starts.
    SeasonDayTypeSchedules: Schedules that use this Season.
    """

    endDate: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
    )

    startDate: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
    )

    # *Association not used*
    # Type M:0..n in CIM
    # SeasonDayTypeSchedules : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
