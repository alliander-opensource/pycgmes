"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class RegularTimePoint(Base):
    """
    Time point for a schedule where the time between the consecutive points is constant.

    sequenceNumber: The position of the regular time point in the sequence. Note that time points don`t have to be
      sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is
      computed by multiplying the associated regular interval schedule`s time step with the regular
      time point sequence number and adding the associated schedules start time. To specify values
      for the start time, use sequence number 0.  The sequence number cannot be negative.
    value1: The first value at the time. The meaning of the value is defined by the derived type of the associated
      schedule.
    value2: The second value at the time. The meaning of the value is defined by the derived type of the associated
      schedule.
    IntervalSchedule: Regular interval schedule containing this time point.
    """

    sequenceNumber: int = 0  # Type #Integer in CIM
    value1: float = 0.0  # Type #Float in CIM
    value2: float = 0.0  # Type #Float in CIM
    IntervalSchedule: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=RegularTimePoint"]
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
            "sequenceNumber": [
                Profile.EQ.value,
            ],
            "value1": [
                Profile.EQ.value,
            ],
            "value2": [
                Profile.EQ.value,
            ],
            "IntervalSchedule": [
                Profile.EQ.value,
            ],
        }
