"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
class DynamicsFunctionBlock(IdentifiedObject):
    """
    Abstract parent class for all Dynamics function blocks.

    enabled: Function block used indicator. true = use of function block is enabled false = use of function block is
      disabled.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    enabled: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=DynamicsFunctionBlock\n"
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
                self.profiles.DY.value,
            ],
            # Attributes
            "enabled": [
                self.profiles.DY.value,
            ],
        }
