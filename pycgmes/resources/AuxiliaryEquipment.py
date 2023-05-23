"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Equipment import Equipment


@dataclass
class AuxiliaryEquipment(Equipment):
    """
    AuxiliaryEquipment describe equipment that is not performing any primary functions but support for the equipment
      performing the primary function. AuxiliaryEquipment is attached to primary equipment via an association with
      Terminal.

    Terminal: The Terminal at the equipment where the AuxiliaryEquipment is attached.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    Terminal: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=AuxiliaryEquipment\n"
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
            ],
            # Attributes
            "Terminal": [
                self.profiles.EQ.value,
            ],
        }
