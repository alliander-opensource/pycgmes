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
class DCTopologicalNode(IdentifiedObject, ModuleType):
    """
    DC bus.

    DCTerminals: See association end TopologicalNode.Terminal.
    DCEquipmentContainer: The connectivity node container to which the topological node belongs.
    DCNodes: The DC connectivity nodes combined together to form this DC topological node.  May depend on the current
      state of switches in the network.
    DCTopologicalIsland: A DC topological node belongs to a DC topological island.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return DCTopologicalNode(*args, **kwargs)

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # DCTerminals : list = Field(default_factory=list, in_profiles = [Profile.TP, ])

    DCEquipmentContainer: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.TP,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # DCNodes : list = Field(default_factory=list, in_profiles = [Profile.TP, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # DCTopologicalIsland : Optional[str] = Field(default=None, in_profiles = [Profile.SV, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.SV,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import DCTopologicalNode"
# work as well as
# "from DCTopologicalNode import DCTopologicalNode".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = DCTopologicalNode
