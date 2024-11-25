"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from ..utils.base import Base
from .String import String


@dataclass
class TownDetail(Base):
    """
    Town details, in the context of address.

    code: Town code.
    country: Name of the country.
    name: Town name.
    section: Town section. For example, it is common for there to be 36 sections per township.
    stateOrProvince: Name of the state or province.
    """

    code: str = Field(
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

    country: str = Field(
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

    name: str = Field(
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

    section: str = Field(
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

    stateOrProvince: str = Field(
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
