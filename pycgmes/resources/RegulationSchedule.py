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
class RegulationSchedule(SeasonDayTypeSchedule):
    """
    A pre-established pattern over time for a controlled variable, e.g., busbar voltage.

    RegulatingControl: Regulating controls that have this schedule.
    """

    RegulatingControl: Optional[str] = Field(
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
