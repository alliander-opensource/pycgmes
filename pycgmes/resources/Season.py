"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class Season(IdentifiedObject):
    """
    A specified time period of the year.

    endDate: Date season ends.
    startDate: Date season starts.
    SeasonDayTypeSchedules: Schedules that use this Season.
    """

    endDate: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    startDate: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # SeasonDayTypeSchedules : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
