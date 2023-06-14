"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .MeasurementValue import MeasurementValue


@dataclass(config=DataclassConfig)
class AnalogValue(MeasurementValue):
    """
    AnalogValue represents an analog MeasurementValue.

    Analog: Measurement to which this value is connected.
    AnalogControl: The Control variable associated with the MeasurementValue.
    """

    Analog: Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # AnalogControl : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=AnalogValue"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "Analog": [
                Profile.OP.value,
            ],
            "AnalogControl": [
                Profile.OP.value,
            ],
        }
