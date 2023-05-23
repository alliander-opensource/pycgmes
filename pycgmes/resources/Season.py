"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
class Season(IdentifiedObject):
    """
    A specified time period of the year.

    endDate: Date season ends.
    startDate: Date season starts.
    SeasonDayTypeSchedules: Schedules that use this Season.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    endDate: float = 0.0  # Type #MonthDay in CIM
    startDate: float = 0.0  # Type #MonthDay in CIM
    # *Association not used*
    # SeasonDayTypeSchedules : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=Season\n"
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
            "endDate": [
                self.profiles.EQ.value,
            ],
            "startDate": [
                self.profiles.EQ.value,
            ],
            "SeasonDayTypeSchedules": [
                self.profiles.EQ.value,
            ],
        }
