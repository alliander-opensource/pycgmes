"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Quality61850 import Quality61850


@dataclass(config=DataclassConfig)
class MeasurementValueQuality(Quality61850):
    """
    Measurement quality flags. Bits 0-10 are defined for substation automation in IEC 61850-7-3. Bits 11-15 are reserved
      for future expansion by that document. Bits 16-31 are reserved for EMS applications.

    MeasurementValue: A MeasurementValue has a MeasurementValueQuality associated with it.
    """

    MeasurementValue: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=MeasurementValueQuality"]
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
                Profile.OP.value,
            ],
            # Attributes
            "MeasurementValue": [
                Profile.OP.value,
            ],
        }
