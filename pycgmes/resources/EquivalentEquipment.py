"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .ConductingEquipment import ConductingEquipment


@dataclass
class EquivalentEquipment(ConductingEquipment):
    """
    The class represents equivalent objects that are the result of a network reduction. The class is the base for
      equivalent objects of different types.

    EquivalentNetwork: The equivalent where the reduced model belongs.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    EquivalentNetwork: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=EquivalentEquipment\n"
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
                self.profiles.SC.value,
                self.profiles.SSH.value,
            ],
            # Attributes
            "EquivalentNetwork": [
                self.profiles.EQ.value,
            ],
        }
