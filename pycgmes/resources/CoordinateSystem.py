"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    crsUrn: str = ""  # Type #String in CIM
    # *Association not used*
    # Locations : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=CoordinateSystem\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.GL.value,
            ],
            # Attributes
            "crsUrn": [
                self.profiles.GL.value,
            ],
            "Locations": [
                self.profiles.GL.value,
            ],
        }
