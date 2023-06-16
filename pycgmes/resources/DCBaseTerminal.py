"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ACDCTerminal import ACDCTerminal


@dataclass(config=DataclassConfig)
class DCBaseTerminal(ACDCTerminal):
    """
    An electrical connection point at a piece of DC conducting equipment. DC terminals are connected at one physical DC
      node that may have multiple DC terminals connected. A DC node is similar to an AC connectivity node. The model
      requires that DC connections are distinct from AC connections.

    DCTopologicalNode: See association end Terminal.TopologicalNode.
    DCNode: The DC connectivity node to which this DC base terminal connects with zero impedance.
    """

    DCTopologicalNode: Optional[str] = None  # Type M:1 in CIM
    DCNode: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=DCBaseTerminal"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.SSH.value,
            ],
            # Attributes
            "DCTopologicalNode": [
                Profile.TP.value,
            ],
            "DCNode": [
                Profile.EQ.value,
            ],
        }
