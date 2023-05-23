"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Base import Base


@dataclass
class SvSwitch(Base):
    """
    State variable for switch.

    open: The attribute tells if the computed state of the switch is considered open.
    Switch: The switch associated with the switch state.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    open: bool = False  # Type #Boolean in CIM
    Switch: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=SvSwitch\n"
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
                self.profiles.SV.value,
            ],
            # Attributes
            "open": [
                self.profiles.SV.value,
            ],
            "Switch": [
                self.profiles.SV.value,
            ],
        }
