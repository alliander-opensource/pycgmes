"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Limit import Limit


@dataclass(config=DataclassConfig)
class AnalogLimit(Limit):
    """
    Limit values for Analog measurements.

    value: The value to supervise against.
    LimitSet: The set of limits.
    """

    value: float = 0.0  # Type #Float in CIM
    LimitSet: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=AnalogLimit"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "value": [
                Profile.OP.value,
            ],
            "LimitSet": [
                Profile.OP.value,
            ],
        }
