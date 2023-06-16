"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .BasicIntervalSchedule import BasicIntervalSchedule


@dataclass(config=DataclassConfig)
class RegularIntervalSchedule(BasicIntervalSchedule):
    """
    The schedule has time points where the time between them is constant.

    TimePoints: The regular interval time point data values that define this schedule.
    timeStep: The time between each pair of subsequent regular time points in sequence order.
    endTime: The time for the last time point.  The value can be a time of day, not a specific date.
    """

    # *Association not used*
    # TimePoints : list = field(default_factory=list)  # Type M:1..n in CIM
    timeStep: int = 0  # Type #Seconds in CIM
    endTime: str = ""  # Type #DateTime in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=RegularIntervalSchedule"]
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
            "TimePoints": [
                Profile.EQ.value,
            ],
            "timeStep": [
                Profile.EQ.value,
            ],
            "endTime": [
                Profile.EQ.value,
            ],
        }
