"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .LoadGroup import LoadGroup


@dataclass(config=DataclassConfig)
class NonConformLoadGroup(LoadGroup, ModuleType):
    """
    Loads that do not follow a daily and seasonal load variation pattern.

    EnergyConsumers: Conform loads assigned to this ConformLoadGroup.
    NonConformLoadSchedules: The NonConformLoadSchedules in the NonConformLoadGroup.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return NonConformLoadGroup(*args, **kwargs)

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # EnergyConsumers : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # NonConformLoadSchedules : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

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
# "import NonConformLoadGroup"
# work as well as
# "from NonConformLoadGroup import NonConformLoadGroup".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = NonConformLoadGroup
