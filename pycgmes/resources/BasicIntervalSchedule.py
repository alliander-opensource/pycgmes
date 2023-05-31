"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
class BasicIntervalSchedule(IdentifiedObject):
    """
    Schedule of values at points in time.

    startTime: The time for the first time point.  The value can be a time of day, not a specific date.
    value1Unit: Value1 units of measure.
    value2Unit: Value2 units of measure.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    startTime: str = ""  # Type #DateTime in CIM
    value1Unit: Optional[str] = None  # Type M:1..1 in CIM
    value2Unit: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=BasicIntervalSchedule\n"
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
            "startTime": [
                self.profiles.EQ.value,
            ],
            "value1Unit": [
                self.profiles.EQ.value,
            ],
            "value2Unit": [
                self.profiles.EQ.value,
            ],
        }
