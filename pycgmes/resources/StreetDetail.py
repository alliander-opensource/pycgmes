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
class StreetDetail(Base):
    """
    Street details, in the context of address.

    addressGeneral: First line of a free form address or some additional address information (for example a mail stop).
    addressGeneral2: (if applicable) Second line of a free form address.
    addressGeneral3: (if applicable) Third line of a free form address.
    buildingName: (if applicable) In certain cases the physical location of the place of interest does not have a direct
      point of entry from the street, but may be located inside a larger structure such as a building,
      complex, office block, apartment, etc.
    code: (if applicable) Utilities often make use of external reference systems, such as those of the town-planner`s
      department or surveyor general`s mapping system, that allocate global reference codes to streets.
    floorIdentification: The identification by name or number, expressed as text, of the floor in the building as part
      of this address.
    name: Name of the street.
    number: Designator of the specific location on the street.
    prefix: Prefix to the street name. For example: North, South, East, West.
    suffix: Suffix to the street name. For example: North, South, East, West.
    suiteNumber: Number of the apartment or suite.
    type: Type of street. Examples include: street, circle, boulevard, avenue, road, drive, etc.
    withinTownLimits: True if this street is within the legal geographical boundaries of the specified town (default).
    """

    addressGeneral: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
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

    addressGeneral2: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
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

    addressGeneral3: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
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

    buildingName: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
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

    code: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
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

    floorIdentification: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
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
                Profile.GL,
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

    number: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
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

    prefix: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
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

    suffix: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
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

    suiteNumber: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
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

    type: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
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

    withinTownLimits: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Boolean",
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
