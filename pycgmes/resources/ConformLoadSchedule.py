"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .SeasonDayTypeSchedule import SeasonDayTypeSchedule


@dataclass
class ConformLoadSchedule(SeasonDayTypeSchedule):
    """
    A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for
      each unit of the period covered. This curve represents a typical pattern of load over the time period for a
      given day type and season.

    ConformLoadGroup: The ConformLoadGroup where the ConformLoadSchedule belongs.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ConformLoadGroup: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ConformLoadSchedule\n"
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
            "ConformLoadGroup": [
                self.profiles.EQ.value,
            ],
        }
