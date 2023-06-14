"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
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

    ConformLoadGroup: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ConformLoadSchedule"]
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
            "ConformLoadGroup": [
                Profile.EQ.value,
            ],
        }
