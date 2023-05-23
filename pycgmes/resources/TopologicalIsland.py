"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
class TopologicalIsland(IdentifiedObject):
    """
    An electrically connected subset of the network. Topological islands can change as the current network state
      changes, e.g. due to:  - disconnect switches or breakers changing state in a SCADA/EMS. - manual creation,
      change or deletion of topological nodes in a planning tool. Only energised TopologicalNode-s shall be part of
      the topological island.

    AngleRefTopologicalNode: The angle reference for the island.   Normally there is one TopologicalNode that is
      selected as the angle reference for each island.   Other reference schemes exist, so
      the association is typically optional.
    TopologicalNodes: A topological node belongs to a topological island.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    AngleRefTopologicalNode: Optional[str] = None  # Type M:1 in CIM
    TopologicalNodes: list = field(default_factory=list)  # Type M:1..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=TopologicalIsland\n"
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
                self.profiles.SV.value,
            ],
            # Attributes
            "AngleRefTopologicalNode": [
                self.profiles.SV.value,
            ],
            "TopologicalNodes": [
                self.profiles.SV.value,
            ],
        }
