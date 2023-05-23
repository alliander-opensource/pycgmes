"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Quality61850 import Quality61850


@dataclass
class MeasurementValueQuality(Quality61850):
    """
    Measurement quality flags. Bits 0-10 are defined for substation automation in IEC 61850-7-3. Bits 11-15 are reserved
      for future expansion by that document. Bits 16-31 are reserved for EMS applications.

    MeasurementValue: A MeasurementValue has a MeasurementValueQuality associated with it.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    MeasurementValue: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=MeasurementValueQuality\n"
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
                self.profiles.OP.value,
            ],
            # Attributes
            "MeasurementValue": [
                self.profiles.OP.value,
            ],
        }
