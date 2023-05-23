"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .EnergyArea import EnergyArea


@dataclass
class LoadArea(EnergyArea):
    """
    The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow
      load scaling.

    SubLoadAreas: The SubLoadAreas in the LoadArea.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # SubLoadAreas : list = field(default_factory=list)  # Type M:1..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=LoadArea\n"
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
            "SubLoadAreas": [
                self.profiles.EQ.value,
            ],
        }
