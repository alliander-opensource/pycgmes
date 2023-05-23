"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .SeasonDayTypeSchedule import SeasonDayTypeSchedule


@dataclass
class SwitchSchedule(SeasonDayTypeSchedule):
    """
    A schedule of switch positions.  If RegularTimePoint.value1 is 0, the switch is open.  If 1, the switch is closed.

    Switch: A SwitchSchedule is associated with a Switch.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    Switch: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=SwitchSchedule\n"
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
            "Switch": [
                self.profiles.EQ.value,
            ],
        }
