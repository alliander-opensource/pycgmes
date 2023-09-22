"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .ConnectivityNodeContainer import ConnectivityNodeContainer


@dataclass(config=DataclassConfig)
class EquivalentNetwork(ConnectivityNodeContainer, ModuleType):
    """
    A class that groups electrical equivalents, including internal nodes, of a network that has been reduced. The
      ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The
      boundary Connectivity nodes where the equivalent connects outside itself are not contained by the equivalent.

    EquivalentEquipments: The associated reduced equivalents.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return EquivalentNetwork(*args, **kwargs)

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # EquivalentEquipments : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import EquivalentNetwork"
# work as well as
# "from EquivalentNetwork import EquivalentNetwork".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = EquivalentNetwork
