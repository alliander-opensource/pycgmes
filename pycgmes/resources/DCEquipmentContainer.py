"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .EquipmentContainer import EquipmentContainer


@dataclass
class DCEquipmentContainer(EquipmentContainer):
    """
    A modelling construct to provide a root class for containment of DC as well as AC equipment. The class differ from
      the EquipmentContaner for AC in that it may also contain DCNode-s. Hence it can contain both AC and DC
      equipment.

    DCTopologicalNode: The topological nodes which belong to this connectivity node container.
    DCNodes: The DC nodes contained in the DC equipment container.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # DCTopologicalNode : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # DCNodes : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=DCEquipmentContainer\n"
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
                self.profiles.EQ.value,
            ],
            # Attributes
            "DCTopologicalNode": [
                self.profiles.TP.value,
            ],
            "DCNodes": [
                self.profiles.EQ.value,
            ],
        }
