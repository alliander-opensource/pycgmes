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
class BusNameMarker(IdentifiedObject, ModuleType):
    """
    Used to apply user standard names to TopologicalNodes. Associated with one or more terminals that are normally
      connected with the bus name.    The associated terminals are normally connected by non-retained switches. For
      a ring bus station configuration, all BusbarSection terminals in the ring are typically associated.   For a
      breaker and a half scheme, both BusbarSections would normally be associated.  For a ring bus, all
      BusbarSections would normally be associated.  For a "straight" busbar configuration, normally only the main
      terminal at the BusbarSection would be associated.

    Terminal: The terminals associated with this bus name marker.
    priority: Priority of bus name marker for use as topology bus name.  Use 0 for do not care.  Use 1 for highest
      priority.  Use 2 as priority is less than 1 and so on.
    ReportingGroup: The reporting group to which this bus name marker belongs.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return BusNameMarker(*args, **kwargs)

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # Terminal : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    priority: int = Field(
        default=0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    ReportingGroup: Optional[str] = Field(
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
            Profile.EQ,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import BusNameMarker"
# work as well as
# "from BusNameMarker import BusNameMarker".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = BusNameMarker
