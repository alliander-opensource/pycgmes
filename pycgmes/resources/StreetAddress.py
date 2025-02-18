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
class StreetAddress(Base):
    """
    General purpose street and postal address information.

    language: The language in which the address is specified, using ISO 639-1 two digit language code.
    poBox: Post office box.
    postalCode: Postal code for the address.
    status: Status of this address.
    streetDetail: Street detail.
    townDetail: Town detail.
    """

    language: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    poBox: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    postalCode: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    status: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    streetDetail: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    townDetail: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
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
