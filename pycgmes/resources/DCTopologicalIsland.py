"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class DCTopologicalIsland(IdentifiedObject, ModuleType):
    """
    An electrically connected subset of the network. DC topological islands can change as the current network state
      changes, e.g. due to:  - disconnect switches or breakers changing state in a SCADA/EMS. - manual creation,
      change or deletion of topological nodes in a planning tool. Only energised TopologicalNode-s shall be part of
      the topological island.

    DCTopologicalNodes: The DC topological nodes in a DC topological island.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return DCTopologicalIsland(*args, **kwargs)

    DCTopologicalNodes: list = Field(
        default_factory=list,
        in_profiles=[
            Profile.SV,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.SV,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import DCTopologicalIsland"
# work as well as
# "from DCTopologicalIsland import DCTopologicalIsland".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = DCTopologicalIsland
