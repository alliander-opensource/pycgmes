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
class Temperature(Base):
    """
    Value of temperature in degrees Celsius.

    multiplier:
    unit:
    value:
    """

    multiplier: Optional[str] = None  # Type M:0..1 in CIM
    unit: Optional[str] = None  # Type M:0..1 in CIM
    value: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=Temperature"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.SC.value,
                Profile.DY.value,
            ],
            # Attributes
            "multiplier": [
                Profile.SC.value,
                Profile.DY.value,
            ],
            "unit": [
                Profile.SC.value,
                Profile.DY.value,
            ],
            "value": [
                Profile.SC.value,
                Profile.DY.value,
            ],
        }
