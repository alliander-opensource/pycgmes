"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Control import Control


@dataclass(config=DataclassConfig)
class AnalogControl(Control):
    """
    An analog control used for supervisory control.

    maxValue: Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    minValue: Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    AnalogValue: The MeasurementValue that is controlled.
    """

    maxValue: float = 0.0  # Type #Float in CIM
    minValue: float = 0.0  # Type #Float in CIM
    AnalogValue: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=AnalogControl"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "maxValue": [
                Profile.OP.value,
            ],
            "minValue": [
                Profile.OP.value,
            ],
            "AnalogValue": [
                Profile.OP.value,
            ],
        }
