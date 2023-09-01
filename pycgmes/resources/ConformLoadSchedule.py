"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .SeasonDayTypeSchedule import SeasonDayTypeSchedule


@dataclass(config=DataclassConfig)
class ConformLoadSchedule(SeasonDayTypeSchedule):
    """
    A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for
      each unit of the period covered. This curve represents a typical pattern of load over the time period for a
      given day type and season.

    ConformLoadGroup: The ConformLoadGroup where the ConformLoadSchedule belongs.
    """

    ConformLoadGroup: Optional[str] = Field(
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
