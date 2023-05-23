"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Limit import Limit


@dataclass
class AnalogLimit(Limit):
    """
    Limit values for Analog measurements.

    value: The value to supervise against.
    LimitSet: The set of limits.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    value: float = 0.0  # Type #Float in CIM
    LimitSet: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=AnalogLimit\n"
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
            "value": [
                self.profiles.OP.value,
            ],
            "LimitSet": [
                self.profiles.OP.value,
            ],
        }
