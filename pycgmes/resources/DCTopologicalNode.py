"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
class DCTopologicalNode(IdentifiedObject):
    """
    DC bus.

    DCTerminals: See association end TopologicalNode.Terminal.
    DCEquipmentContainer: The connectivity node container to which the topological node belongs.
    DCNodes: The DC connectivity nodes combined together to form this DC topological node.  May depend on the current
      state of switches in the network.
    DCTopologicalIsland: A DC topological node belongs to a DC topological island.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # DCTerminals : list = field(default_factory=list)  # Type M:0..n in CIM
    DCEquipmentContainer: Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # DCNodes : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # DCTopologicalIsland : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=DCTopologicalNode\n"
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
                self.profiles.TP.value,
                self.profiles.SV.value,
            ],
            # Attributes
            "DCTerminals": [
                self.profiles.TP.value,
            ],
            "DCEquipmentContainer": [
                self.profiles.TP.value,
            ],
            "DCNodes": [
                self.profiles.TP.value,
            ],
            "DCTopologicalIsland": [
                self.profiles.SV.value,
            ],
        }
