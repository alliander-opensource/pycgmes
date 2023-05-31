"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Control import Control


@dataclass
class Command(Control):
    """
    A Command is a discrete control used for supervisory control.

    normalValue: Normal value for Control.value e.g. used for percentage scaling.
    value: The value representing the actuator output.
    ValueAliasSet: The ValueAliasSet used for translation of a Control value to a name.
    DiscreteValue: The MeasurementValue that is controlled.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    normalValue: int = 0  # Type #Integer in CIM
    value: int = 0  # Type #Integer in CIM
    ValueAliasSet: Optional[str] = None  # Type M:0..1 in CIM
    DiscreteValue: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=Command\n"
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
            "ValueAliasSet": [
                self.profiles.OP.value,
            ],
            "DiscreteValue": [
                self.profiles.OP.value,
            ],
        }
