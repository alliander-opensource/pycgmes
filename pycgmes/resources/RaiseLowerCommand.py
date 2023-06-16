"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .AnalogControl import AnalogControl


@dataclass(config=DataclassConfig)
class RaiseLowerCommand(AnalogControl):
    """
    An analog control that increases or decreases a set point value with pulses. Unless otherwise specified, one pulse
      moves the set point by one.

    ValueAliasSet: The ValueAliasSet used for translation of a Control value to a name.
    """

    ValueAliasSet: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=RaiseLowerCommand"]
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
            "ValueAliasSet": [
                Profile.OP.value,
            ],
        }
