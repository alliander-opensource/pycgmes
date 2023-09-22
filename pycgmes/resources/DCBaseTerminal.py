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

from .ACDCTerminal import ACDCTerminal


@dataclass(config=DataclassConfig)
class DCBaseTerminal(ACDCTerminal, ModuleType):
    """
    An electrical connection point at a piece of DC conducting equipment. DC terminals are connected at one physical DC
      node that may have multiple DC terminals connected. A DC node is similar to an AC connectivity node. The model
      requires that DC connections are distinct from AC connections.

    DCTopologicalNode: See association end Terminal.TopologicalNode.
    DCNode: The DC connectivity node to which this DC base terminal connects with zero impedance.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return DCBaseTerminal(*args, **kwargs)

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
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.EQ,
            Profile.SSH,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import DCBaseTerminal"
# work as well as
# "from DCBaseTerminal import DCBaseTerminal".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = DCBaseTerminal
