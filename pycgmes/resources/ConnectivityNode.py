"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class ConnectivityNode(IdentifiedObject, ModuleType):
    """
    Connectivity nodes are points where terminals of AC conducting equipment are connected together with zero impedance.

    TopologicalNode: The topological node to which this connectivity node is assigned.  May depend on the current state
      of switches in the network.
    BoundaryPoint: The boundary point associated with the connectivity node.
    Terminals: Terminals interconnected with zero impedance at a this connectivity node.
    ConnectivityNodeContainer: Container of this connectivity node.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ConnectivityNode(*args, **kwargs)

    TopologicalNode: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.TP,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # BoundaryPoint : Optional[str] = Field(default=None, in_profiles = [Profile.EQBD, Profile.EQ, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Terminals : list = Field(default_factory=list, in_profiles = [Profile.EQBD, Profile.EQ, ])

    ConnectivityNodeContainer: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQBD,
            Profile.EQ,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.EQBD,
            Profile.EQ,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import ConnectivityNode"
# work as well as
# "from ConnectivityNode import ConnectivityNode".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ConnectivityNode
