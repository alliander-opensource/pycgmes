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
from .Base import DataclassConfig, Profile
from .RegularIntervalSchedule import RegularIntervalSchedule


@dataclass(config=DataclassConfig)
class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """
    A time schedule covering a 24 hour period, with curve data for a specific type of season and day.

    DayType: DayType for the Schedule.
    Season: Season for the Schedule.
    """

    DayType: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    Season: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
