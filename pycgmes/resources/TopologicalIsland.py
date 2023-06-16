"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import field, fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
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

    AngleRefTopologicalNode: Optional[str] = None  # Type M:1 in CIM
    TopologicalNodes: list = field(default_factory=list)  # Type M:1..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=TopologicalIsland"]
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
                Profile.SV.value,
            ],
            # Attributes
            "AngleRefTopologicalNode": [
                Profile.SV.value,
            ],
            "TopologicalNodes": [
                Profile.SV.value,
            ],
        }
