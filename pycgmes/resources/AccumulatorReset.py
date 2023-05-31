"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Control import Control


@dataclass
class AccumulatorReset(Control):
    """
    This command resets the counter value to zero.

    AccumulatorValue: The accumulator value that is reset by the command.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    AccumulatorValue: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=AccumulatorReset\n"
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
            "AccumulatorValue": [
                self.profiles.OP.value,
            ],
        }
