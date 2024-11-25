"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .IdentifiedObject import IdentifiedObject
from .String import String


@dataclass
class CoordinateSystem(IdentifiedObject):
    """
    Coordinate reference system.

    Locations: All locations described with position points in this coordinate system.
    crsUrn: A Uniform Resource Name (URN) for the coordinate reference system (crs) used to define
      `Location.PositionPoints`. An example would be the European Petroleum Survey Group (EPSG) code for a
      coordinate reference system, defined in URN under the Open Geospatial Consortium (OGC) namespace as:
      urn:ogc:def:crs:EPSG::XXXX, where XXXX is an EPSG code (a full list of codes can be found at the EPSG
      Registry web site http://www.epsg-registry.org/). To define the coordinate system as being WGS84
      (latitude, longitude) using an EPSG OGC, this attribute would be urn:ogc:def:crs:EPSG::4236. A profile
      should limit this code to a set of allowed URNs agreed to by all sending and receiving parties.
    """

    Locations: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    crsUrn: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": String,
        },
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.GL,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.GL
