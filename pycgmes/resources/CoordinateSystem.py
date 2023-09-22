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
class CoordinateSystem(IdentifiedObject, ModuleType):
    """
    Coordinate reference system.

    crsUrn: A Uniform Resource Name (URN) for the coordinate reference system (crs) used to define
      `Location.PositionPoints`. An example would be the European Petroleum Survey Group (EPSG) code for a
      coordinate reference system, defined in URN under the Open Geospatial Consortium (OGC) namespace as:
      urn:ogc:def:crs:EPSG::XXXX, where XXXX is an EPSG code (a full list of codes can be found at the EPSG
      Registry web site http://www.epsg-registry.org/). To define the coordinate system as being WGS84
      (latitude, longitude) using an EPSG OGC, this attribute would be urn:ogc:def:crs:EPSG::4236. A profile
      should limit this code to a set of allowed URNs agreed to by all sending and receiving parties.
    Locations: All locations described with position points in this coordinate system.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return CoordinateSystem(*args, **kwargs)

    crsUrn: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Locations : list = Field(default_factory=list, in_profiles = [Profile.GL, ])

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
# "import CoordinateSystem"
# work as well as
# "from CoordinateSystem import CoordinateSystem".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = CoordinateSystem
