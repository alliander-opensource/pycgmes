"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
class ConnectivityNode(IdentifiedObject):
    """
    Connectivity nodes are points where terminals of AC conducting equipment are connected together with zero impedance.

    TopologicalNode: The topological node to which this connectivity node is assigned.  May depend on the current state
      of switches in the network.
    BoundaryPoint: The boundary point associated with the connectivity node.
    Terminals: Terminals interconnected with zero impedance at a this connectivity node.
    ConnectivityNodeContainer: Container of this connectivity node.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    TopologicalNode: Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # BoundaryPoint : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # Terminals : list = field(default_factory=list)  # Type M:0..n in CIM
    ConnectivityNodeContainer: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ConnectivityNode\n"
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
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            # Attributes
            "TopologicalNode": [
                self.profiles.TP.value,
            ],
            "BoundaryPoint": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "Terminals": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "ConnectivityNodeContainer": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
        }
