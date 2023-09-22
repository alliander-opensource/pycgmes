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
class GeographicalRegion(IdentifiedObject, ModuleType):
    """
    A geographical region of a power system network model.

    Regions: All sub-geographical regions within this geographical region.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return GeographicalRegion(*args, **kwargs)

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Regions : list = Field(default_factory=list, in_profiles = [Profile.EQBD, Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQBD,
            Profile.EQ,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import GeographicalRegion"
# work as well as
# "from GeographicalRegion import GeographicalRegion".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = GeographicalRegion
