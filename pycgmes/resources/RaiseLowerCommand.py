"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .AnalogControl import AnalogControl


@dataclass
class RaiseLowerCommand(AnalogControl):
    """
    An analog control that increases or decreases a set point value with pulses. Unless otherwise specified, one pulse
      moves the set point by one.

    ValueAliasSet: The ValueAliasSet used for translation of a Control value to a name.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ValueAliasSet: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=RaiseLowerCommand\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.OP.value,
            ],
            # Attributes
            "ValueAliasSet": [
                self.profiles.OP.value,
            ],
        }
