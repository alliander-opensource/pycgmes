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
from .BasicIntervalSchedule import BasicIntervalSchedule


@dataclass
class RegularIntervalSchedule(BasicIntervalSchedule):
    """
    The schedule has time points where the time between them is constant.

    TimePoints: The regular interval time point data values that define this schedule.
    timeStep: The time between each pair of subsequent regular time points in sequence order.
    endTime: The time for the last time point.  The value can be a time of day, not a specific date.
    """

    # *Association not used*
    # Type M:1..n in CIM
    # TimePoints : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]})

    timeStep: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
    )

    endTime: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
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
        }
