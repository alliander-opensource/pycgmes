# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class CoordinateSystem(IdentifiedObject):
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
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.GL,
        }
