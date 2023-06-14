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
class PerCent(Base):
    """
    Percentage on a defined base.   For example, specify as 100 to indicate at the defined base.

    value: Normally 0 to 100 on a defined base.
    unit:
    multiplier:
    """

    value: float = 0.0  # Type #Float in CIM
    unit: Optional[str] = None  # Type M:0..1 in CIM
    multiplier: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PerCent"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.SC.value,
                Profile.SSH.value,
                Profile.OP.value,
            ],
            # Attributes
            "value": [
                Profile.EQ.value,
                Profile.SC.value,
                Profile.SSH.value,
                Profile.OP.value,
            ],
            "unit": [
                Profile.EQ.value,
                Profile.SC.value,
                Profile.SSH.value,
                Profile.OP.value,
            ],
            "multiplier": [
                Profile.EQ.value,
                Profile.SC.value,
                Profile.SSH.value,
                Profile.OP.value,
            ],
        }
