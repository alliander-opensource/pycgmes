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
class SvTapStep(Base):
    """
    State variable for transformer tap step.

    position: The floating point tap position.   This is not the tap ratio, but rather the tap step position as defined
      by the related tap changer model and normally is constrained to be within the range of minimum and
      maximum tap positions.
    TapChanger: The tap changer associated with the tap step state.
    """

    position: float = 0.0  # Type #Float in CIM
    TapChanger: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=SvTapStep"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.SV.value,
            ],
            # Attributes
            "position": [
                Profile.SV.value,
            ],
            "TapChanger": [
                Profile.SV.value,
            ],
        }
