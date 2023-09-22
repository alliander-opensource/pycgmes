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
class DCNode(IdentifiedObject, ModuleType):
    """
    DC nodes are points where terminals of DC conducting equipment are connected together with zero impedance.

    DCTopologicalNode: The DC topological node to which this DC connectivity node is assigned.  May depend on the
      current state of switches in the network.
    DCTerminals: DC base terminals interconnected with zero impedance at a this DC connectivity node.
    DCEquipmentContainer: The DC container for the DC nodes.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return DCNode(*args, **kwargs)

    DCTopologicalNode: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.TP,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # DCTerminals : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    DCEquipmentContainer: Optional[str] = Field(
        default=None,
        in_profiles=[
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
            Profile.EQ,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import DCNode"
# work as well as
# "from DCNode import DCNode".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = DCNode
