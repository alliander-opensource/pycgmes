"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .PowerSystemResource import PowerSystemResource


@dataclass(config=DataclassConfig)
class ConnectivityNodeContainer(PowerSystemResource, ModuleType):
    """
    A base class for all objects that may contain connectivity nodes or topological nodes.

    TopologicalNode: The topological nodes which belong to this connectivity node container.
    ConnectivityNodes: Connectivity nodes which belong to this connectivity node container.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ConnectivityNodeContainer(*args, **kwargs)

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # TopologicalNode : list = Field(default_factory=list, in_profiles = [Profile.TP, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # ConnectivityNodes : list = Field(default_factory=list, in_profiles = [Profile.EQBD, Profile.EQ, ])

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
# "import ConnectivityNodeContainer"
# work as well as
# "from ConnectivityNodeContainer import ConnectivityNodeContainer".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ConnectivityNodeContainer
