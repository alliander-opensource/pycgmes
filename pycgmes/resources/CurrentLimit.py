"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .OperationalLimit import OperationalLimit


@dataclass
class CurrentLimit(OperationalLimit):
    """
    Operational limit on current.

    normalValue: The normal value for limit on current flow. The attribute shall be a positive value or zero.
    value: Limit on current flow. The attribute shall be a positive value or zero.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    normalValue: float = 0.0  # Type #CurrentFlow in CIM
    value: float = 0.0  # Type #CurrentFlow in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=CurrentLimit\n"
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
                self.profiles.EQ.value,
                self.profiles.SSH.value,
            ],
            # Attributes
            "normalValue": [
                self.profiles.EQ.value,
            ],
            "value": [
                self.profiles.SSH.value,
            ],
        }
