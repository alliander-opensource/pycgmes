"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class BasicIntervalSchedule(IdentifiedObject):
    """
    Schedule of values at points in time.

    startTime: The time for the first time point.  The value can be a time of day, not a specific date.
    value1Unit: Value1 units of measure.
    value2Unit: Value2 units of measure.
    """

    startTime: str = ""  # Type #DateTime in CIM
    value1Unit: Optional[str] = None  # Type M:1..1 in CIM
    value2Unit: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=BasicIntervalSchedule"]
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
            "startTime": [
                Profile.EQ.value,
            ],
            "value1Unit": [
                Profile.EQ.value,
            ],
            "value2Unit": [
                Profile.EQ.value,
            ],
        }
