"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
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

    DayType: Optional[str] = None  # Type M:1..1 in CIM
    Season: Optional[str] = None  # Type M:1..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=SeasonDayTypeSchedule"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.EQ.value,
            ],
            # Attributes
            "DayType": [
                Profile.EQ.value,
            ],
            "Season": [
                Profile.EQ.value,
            ],
        }
