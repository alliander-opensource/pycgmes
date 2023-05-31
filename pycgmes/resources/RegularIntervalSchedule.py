"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .BasicIntervalSchedule import BasicIntervalSchedule


@dataclass
class RegularIntervalSchedule(BasicIntervalSchedule):
    """
    The schedule has time points where the time between them is constant.

    TimePoints: The regular interval time point data values that define this schedule.
    timeStep: The time between each pair of subsequent regular time points in sequence order.
    endTime: The time for the last time point.  The value can be a time of day, not a specific date.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # TimePoints : list = field(default_factory=list)  # Type M:1..n in CIM
    timeStep: int = 0  # Type #Seconds in CIM
    endTime: str = ""  # Type #DateTime in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=RegularIntervalSchedule\n"
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
            "TimePoints": [
                self.profiles.EQ.value,
            ],
            "timeStep": [
                self.profiles.EQ.value,
            ],
            "endTime": [
                self.profiles.EQ.value,
            ],
        }
