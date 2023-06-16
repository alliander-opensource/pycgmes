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
class ConnectivityNode(IdentifiedObject):
    """
    Connectivity nodes are points where terminals of AC conducting equipment are connected together with zero impedance.

    TopologicalNode: The topological node to which this connectivity node is assigned.  May depend on the current state
      of switches in the network.
    BoundaryPoint: The boundary point associated with the connectivity node.
    Terminals: Terminals interconnected with zero impedance at a this connectivity node.
    ConnectivityNodeContainer: Container of this connectivity node.
    """

    TopologicalNode: Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # BoundaryPoint : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # Terminals : list = field(default_factory=list)  # Type M:0..n in CIM
    ConnectivityNodeContainer: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ConnectivityNode"]
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
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            # Attributes
            "TopologicalNode": [
                Profile.TP.value,
            ],
            "BoundaryPoint": [
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            "Terminals": [
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            "ConnectivityNodeContainer": [
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
        }
