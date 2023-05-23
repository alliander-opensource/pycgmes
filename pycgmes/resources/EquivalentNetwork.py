"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ConnectivityNodeContainer import ConnectivityNodeContainer


@dataclass
class EquivalentNetwork(ConnectivityNodeContainer):
    """
    A class that groups electrical equivalents, including internal nodes, of a network that has been reduced. The
      ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The
      boundary Connectivity nodes where the equivalent connects outside itself are not contained by the equivalent.

    EquivalentEquipments: The associated reduced equivalents.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # EquivalentEquipments : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=EquivalentNetwork\n"
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
            "EquivalentEquipments": [
                self.profiles.EQ.value,
            ],
        }
