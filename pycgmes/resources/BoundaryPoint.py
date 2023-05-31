"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .PowerSystemResource import PowerSystemResource


@dataclass
class BoundaryPoint(PowerSystemResource):
    """
    Designates a connection point at which one or more model authority sets shall connect to. The location of the
      connection point as well as other properties are agreed between organisations responsible for the
      interconnection, hence all attributes of the class represent this agreement.  It is primarily used in a
      boundary model authority set which can contain one or many BoundaryPoint-s among other Equipment-s and their
      connections.

    fromEndIsoCode: The ISO code of the region which the `From` side of the Boundary point belongs to or it is connected
      to. The ISO code is a two-character country code as defined by ISO 3166
      (http://www.iso.org/iso/country_codes). The length of the string is 2 characters maximum.
    fromEndName: A human readable name with length of the string 64 characters maximum. It covers the following two
      cases: -if the Boundary point is placed on a tie-line, it is the name (IdentifiedObject.name) of
      the substation at which the `From` side of the tie-line is connected to. -if the Boundary point
      is placed in a substation, it is the name (IdentifiedObject.name) of the element (e.g.
      PowerTransformer, ACLineSegment, Switch, etc.) at which the `From` side of the Boundary point is
      connected to.
    fromEndNameTso: Identifies the name of the transmission system operator, distribution system operator or other
      entity at which the `From` side of the interconnection is connected to. The length of the
      string is 64 characters maximum.
    toEndIsoCode: The ISO code of the region which the `To` side of the Boundary point belongs to or is connected to.
      The ISO code is a two-character country code as defined by ISO 3166
      (http://www.iso.org/iso/country_codes). The length of the string is 2 characters maximum.
    toEndName: A human readable name with length of the string 64 characters maximum. It covers the following two cases:
      -if the Boundary point is placed on a tie-line, it is the name (IdentifiedObject.name) of the
      substation at which the `To` side of the tie-line is connected to. -if the Boundary point is placed
      in a substation, it is the name (IdentifiedObject.name) of the element (e.g. PowerTransformer,
      ACLineSegment, Switch, etc.) at which the `To` side of the Boundary point is connected to.
    toEndNameTso: Identifies the name of the transmission system operator, distribution system operator or other entity
      at which the `To` side of the interconnection is connected to. The length of the string is 64
      characters maximum.
    isDirectCurrent: If true, this boundary point is a point of common coupling (PCC) of a direct current (DC)
      interconnection, otherwise the interconnection is AC (default).
    isExcludedFromAreaInterchange: If true, this boundary point is on the interconnection that is excluded from control
      area interchange calculation and consequently has no related tie flows.
      Otherwise, the interconnection is included in control area interchange and a
      TieFlow is required at all sides of the boundary point (default).
    ConnectivityNode: The connectivity node that is designated as a boundary point.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    fromEndIsoCode: str = ""  # Type #String in CIM
    fromEndName: str = ""  # Type #String in CIM
    fromEndNameTso: str = ""  # Type #String in CIM
    toEndIsoCode: str = ""  # Type #String in CIM
    toEndName: str = ""  # Type #String in CIM
    toEndNameTso: str = ""  # Type #String in CIM
    isDirectCurrent: bool = False  # Type #Boolean in CIM
    isExcludedFromAreaInterchange: bool = False  # Type #Boolean in CIM
    ConnectivityNode: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=BoundaryPoint\n"
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
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            # Attributes
            "fromEndIsoCode": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "fromEndName": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "fromEndNameTso": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "toEndIsoCode": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "toEndName": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "toEndNameTso": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "isDirectCurrent": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "isExcludedFromAreaInterchange": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "ConnectivityNode": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
        }
