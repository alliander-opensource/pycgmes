"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .ACDCTerminal import ACDCTerminal


@dataclass
class DCBaseTerminal(ACDCTerminal):
    """
    An electrical connection point at a piece of DC conducting equipment. DC terminals are connected at one physical DC
      node that may have multiple DC terminals connected. A DC node is similar to an AC connectivity node. The model
      requires that DC connections are distinct from AC connections.

    DCTopologicalNode: See association end Terminal.TopologicalNode.
    DCNode: The DC connectivity node to which this DC base terminal connects with zero impedance.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    DCTopologicalNode: Optional[str] = None  # Type M:1 in CIM
    DCNode: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=DCBaseTerminal\n"
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
                self.profiles.SSH.value,
            ],
            # Attributes
            "DCTopologicalNode": [
                self.profiles.TP.value,
            ],
            "DCNode": [
                self.profiles.EQ.value,
            ],
        }
