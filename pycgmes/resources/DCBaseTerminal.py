"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
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

    DCTopologicalNode: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.TP,
        ],
    )

    DCNode: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.EQ,
            Profile.SSH,
        }
