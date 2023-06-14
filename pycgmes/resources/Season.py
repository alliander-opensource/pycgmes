"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
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

    endDate: float = 0.0  # Type #MonthDay in CIM
    startDate: float = 0.0  # Type #MonthDay in CIM
    # *Association not used*
    # SeasonDayTypeSchedules : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=Season"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "endDate": [
                Profile.EQ.value,
            ],
            "startDate": [
                Profile.EQ.value,
            ],
            "SeasonDayTypeSchedules": [
                Profile.EQ.value,
            ],
        }
