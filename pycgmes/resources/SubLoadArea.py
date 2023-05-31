"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .EnergyArea import EnergyArea


@dataclass
class SubLoadArea(EnergyArea):
    """
    The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load
      scaling.

    LoadArea: The LoadArea where the SubLoadArea belongs.
    LoadGroups: The Loadgroups in the SubLoadArea.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    LoadArea: Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # LoadGroups : list = field(default_factory=list)  # Type M:1..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=SubLoadArea\n"
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
            "LoadArea": [
                self.profiles.EQ.value,
            ],
            "LoadGroups": [
                self.profiles.EQ.value,
            ],
        }
