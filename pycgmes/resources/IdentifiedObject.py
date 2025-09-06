"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from ..utils.base import Base


@dataclass
class IdentifiedObject(Base):
    """
    This is a root class to provide common identification for all classes needing identification and naming attributes.

    DiagramObjects: The diagram objects that are associated with the domain object.
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
    """

    DiagramObjects: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.DL,
            ],
            "is_used": False,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    description: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
                Profile.DL,
                Profile.DY,
                Profile.EQBD,
                Profile.OP,
                Profile.TP,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "String",
        },
    )

    energyIdentCodeEic: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
                Profile.EQBD,
                Profile.TP,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100-European#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "String",
        },
    )

    mRID: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
                Profile.DL,
                Profile.DY,
                Profile.EQBD,
                Profile.GL,
                Profile.OP,
                Profile.SC,
                Profile.SSH,
                Profile.SV,
                Profile.TP,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "String",
        },
    )

    name: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
                Profile.DL,
                Profile.DY,
                Profile.EQBD,
                Profile.GL,
                Profile.OP,
                Profile.SV,
                Profile.TP,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "String",
        },
    )

    shortName: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
                Profile.EQBD,
                Profile.TP,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100-European#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "String",
        },
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.DL,
            Profile.DY,
            Profile.EQBD,
            Profile.GL,
            Profile.OP,
            Profile.SC,
            Profile.SSH,
            Profile.SV,
            Profile.TP,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
