"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .EquipmentContainer import EquipmentContainer


@dataclass(config=DataclassConfig)
class DCEquipmentContainer(EquipmentContainer):
    """
    A modelling construct to provide a root class for containment of DC as well as AC equipment. The class differ from
      the EquipmentContaner for AC in that it may also contain DCNode-s. Hence it can contain both AC and DC
      equipment.

    DCTopologicalNode: The topological nodes which belong to this connectivity node container.
    DCNodes: The DC nodes contained in the DC equipment container.
    """

    # *Association not used*
    # DCTopologicalNode : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # DCNodes : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=DCEquipmentContainer"]
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
                Profile.EQ.value,
            ],
            # Attributes
            "DCTopologicalNode": [
                Profile.TP.value,
            ],
            "DCNodes": [
                Profile.EQ.value,
            ],
        }
