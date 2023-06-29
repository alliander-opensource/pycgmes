"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
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

    ValueAliasSet: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
