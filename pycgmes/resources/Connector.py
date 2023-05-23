"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ConductingEquipment import ConductingEquipment


@dataclass
class Connector(ConductingEquipment):
    """
    A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment
      within a single substation and are modelled with a single logical terminal.

    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # No attributes defined for this class.

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=Connector\n"
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
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
                self.profiles.SC.value,
            ],
            # Attributes
        }
