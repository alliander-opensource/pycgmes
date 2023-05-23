"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .AnalogControl import AnalogControl


@dataclass
class SetPoint(AnalogControl):
    """
    An analog control that issues a set point value.

    normalValue: Normal value for Control.value e.g. used for percentage scaling.
    value: The value representing the actuator output.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    normalValue: float = 0.0  # Type #Float in CIM
    value: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=SetPoint\n"
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
            "normalValue": [
                self.profiles.OP.value,
            ],
            "value": [
                self.profiles.OP.value,
            ],
        }
