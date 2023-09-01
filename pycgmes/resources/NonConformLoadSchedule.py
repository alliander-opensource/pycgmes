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
class NonConformLoadSchedule(SeasonDayTypeSchedule):
    """
    An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming
      loads, e.g., large industrial load or power station service (where modelled).

    NonConformLoadGroup: The NonConformLoadGroup where the NonConformLoadSchedule belongs.
    """

    NonConformLoadGroup: Optional[str] = Field(
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
