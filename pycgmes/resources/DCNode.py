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
class DCNode(IdentifiedObject):
    """
    DC nodes are points where terminals of DC conducting equipment are connected together with zero impedance.

    DCTopologicalNode: The DC topological node to which this DC connectivity node is assigned.  May depend on the
      current state of switches in the network.
    DCTerminals: DC base terminals interconnected with zero impedance at a this DC connectivity node.
    DCEquipmentContainer: The DC container for the DC nodes.
    """

    DCTopologicalNode: Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # DCTerminals : list = field(default_factory=list)  # Type M:0..n in CIM
    DCEquipmentContainer: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=DCNode"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.EQ.value,
            ],
            # Attributes
            "DCTopologicalNode": [
                Profile.TP.value,
            ],
            "DCTerminals": [
                Profile.EQ.value,
            ],
            "DCEquipmentContainer": [
                Profile.EQ.value,
            ],
        }
