"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class IdentifiedObject(Base):
    """
    This is a root class to provide common identification for all classes needing identification and naming attributes.

    description: The description is a free human readable text describing or naming the object. It may be non unique and
      may not correlate to a naming hierarchy.
    energyIdentCodeEic: The attribute is used for an exchange of the EIC code (Energy identification Code). The length
      of the string is 16 characters as defined by the EIC code. For details on EIC scheme
      please refer to ENTSO-E web site.
    mRID: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global
      uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID
      is strongly recommended. For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is
      mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
    name: The name is any free human readable and possibly non unique text naming the object.
    shortName: The attribute is used for an exchange of a human readable short name with length of the string 12
      characters maximum.
    DiagramObjects: The diagram objects that are associated with the domain object.
    """

    description: str = ""  # Type #String in CIM
    energyIdentCodeEic: str = ""  # Type #String in CIM
    mRID: str = ""  # Type #String in CIM
    name: str = ""  # Type #String in CIM
    shortName: str = ""  # Type #String in CIM
    # *Association not used*
    # DiagramObjects : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=IdentifiedObject"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.TP.value,
                Profile.GL.value,
                Profile.DL.value,
                Profile.EQBD.value,
                Profile.EQ.value,
                Profile.SC.value,
                Profile.SV.value,
                Profile.SSH.value,
                Profile.DY.value,
                Profile.OP.value,
            ],
            # Attributes
            "description": [
                Profile.TP.value,
                Profile.DL.value,
                Profile.EQBD.value,
                Profile.EQ.value,
                Profile.DY.value,
                Profile.OP.value,
            ],
            "energyIdentCodeEic": [
                Profile.TP.value,
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            "mRID": [
                Profile.TP.value,
                Profile.GL.value,
                Profile.DL.value,
                Profile.EQBD.value,
                Profile.EQ.value,
                Profile.SC.value,
                Profile.SV.value,
                Profile.SSH.value,
                Profile.DY.value,
                Profile.OP.value,
            ],
            "name": [
                Profile.TP.value,
                Profile.GL.value,
                Profile.DL.value,
                Profile.EQBD.value,
                Profile.EQ.value,
                Profile.SV.value,
                Profile.DY.value,
                Profile.OP.value,
            ],
            "shortName": [
                Profile.TP.value,
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            "DiagramObjects": [
                Profile.DL.value,
            ],
        }
