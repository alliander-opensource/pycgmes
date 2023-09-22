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
class Location(IdentifiedObject, ModuleType):
    """
    The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in
      time. It can be defined with one or more position points (coordinates) in a given coordinate system.

    CoordinateSystem: Coordinate system used to describe position points of this location.
    mainAddress: Main address of the location.
    PowerSystemResources: All power system resources at this location.
    PositionPoints: Sequence of position points describing this location, expressed in coordinate system
      `Location.CoordinateSystem`.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return Location(*args, **kwargs)

    CoordinateSystem: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.GL,
        ],
    )

    mainAddress: float = Field(
        default=0.0,
        in_profiles=[
            Profile.GL,
        ],
    )

    PowerSystemResources: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.GL,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # PositionPoints : list = Field(default_factory=list, in_profiles = [Profile.GL, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.GL,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import Location"
# work as well as
# "from Location import Location".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = Location
