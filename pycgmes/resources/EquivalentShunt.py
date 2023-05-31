"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .EquivalentEquipment import EquivalentEquipment


@dataclass
class EquivalentShunt(EquivalentEquipment):
    """
    The class represents equivalent shunts.

    b: Positive sequence shunt susceptance.
    g: Positive sequence shunt conductance.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    b: float = 0.0  # Type #Susceptance in CIM
    g: float = 0.0  # Type #Conductance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=EquivalentShunt\n"
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
            "b": [
                self.profiles.EQ.value,
            ],
            "g": [
                self.profiles.EQ.value,
            ],
        }
