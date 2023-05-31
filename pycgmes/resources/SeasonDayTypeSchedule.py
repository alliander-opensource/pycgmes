"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .RegularIntervalSchedule import RegularIntervalSchedule


@dataclass
class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """
    A time schedule covering a 24 hour period, with curve data for a specific type of season and day.

    DayType: DayType for the Schedule.
    Season: Season for the Schedule.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    DayType: Optional[str] = None  # Type M:1..1 in CIM
    Season: Optional[str] = None  # Type M:1..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=SeasonDayTypeSchedule\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.EQ.value,
            ],
            # Attributes
            "DayType": [
                self.profiles.EQ.value,
            ],
            "Season": [
                self.profiles.EQ.value,
            ],
        }
