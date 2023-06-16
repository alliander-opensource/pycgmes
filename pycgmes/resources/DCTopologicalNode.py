"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class DCTopologicalNode(IdentifiedObject):
    """
    DC bus.

    DCTerminals: See association end TopologicalNode.Terminal.
    DCEquipmentContainer: The connectivity node container to which the topological node belongs.
    DCNodes: The DC connectivity nodes combined together to form this DC topological node.  May depend on the current
      state of switches in the network.
    DCTopologicalIsland: A DC topological node belongs to a DC topological island.
    """

    # *Association not used*
    # DCTerminals : list = field(default_factory=list)  # Type M:0..n in CIM
    DCEquipmentContainer: Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # DCNodes : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # DCTopologicalIsland : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=DCTopologicalNode"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.TP.value,
                Profile.SV.value,
            ],
            # Attributes
            "DCTerminals": [
                Profile.TP.value,
            ],
            "DCEquipmentContainer": [
                Profile.TP.value,
            ],
            "DCNodes": [
                Profile.TP.value,
            ],
            "DCTopologicalIsland": [
                Profile.SV.value,
            ],
        }
