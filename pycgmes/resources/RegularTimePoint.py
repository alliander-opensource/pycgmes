"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Base import Base


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    sequenceNumber: int = 0  # Type #Integer in CIM
    value1: float = 0.0  # Type #Float in CIM
    value2: float = 0.0  # Type #Float in CIM
    IntervalSchedule: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=RegularTimePoint\n"
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
            "sequenceNumber": [
                self.profiles.EQ.value,
            ],
            "value1": [
                self.profiles.EQ.value,
            ],
            "value2": [
                self.profiles.EQ.value,
            ],
            "IntervalSchedule": [
                self.profiles.EQ.value,
            ],
        }
