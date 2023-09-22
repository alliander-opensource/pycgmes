"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class ReportingGroup(IdentifiedObject, ModuleType):
    """
    A reporting group is used for various ad-hoc groupings used for reporting.

    TopologicalNode: The topological nodes that belong to the reporting group.
    BusNameMarker: The bus name markers that belong to this reporting group.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ReportingGroup(*args, **kwargs)

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # TopologicalNode : list = Field(default_factory=list, in_profiles = [Profile.TP, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # BusNameMarker : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

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
# "import ReportingGroup"
# work as well as
# "from ReportingGroup import ReportingGroup".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ReportingGroup
