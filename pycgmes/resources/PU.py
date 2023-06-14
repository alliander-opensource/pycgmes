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
class PU(Base):
    """
    Per Unit - a positive or negative value referred to a defined base. Values typically range from -10 to +10.

    value:
    unit:
    multiplier:
    """

    value: float = 0.0  # Type #Float in CIM
    unit: Optional[str] = None  # Type M:0..1 in CIM
    multiplier: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PU"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.SSH.value,
                Profile.DY.value,
            ],
            # Attributes
            "value": [
                Profile.SC.value,
                Profile.SSH.value,
                Profile.DY.value,
            ],
            "unit": [
                Profile.SC.value,
                Profile.SSH.value,
                Profile.DY.value,
            ],
            "multiplier": [
                Profile.SC.value,
                Profile.SSH.value,
                Profile.DY.value,
            ],
        }
