"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from ..utils.base import Base
from .Float import Float


@dataclass
class SvTapStep(Base):
    """
    State variable for transformer tap step.

    TapChanger: The tap changer associated with the tap step state.
    position: The floating point tap position.   This is not the tap ratio, but rather the tap step position as defined
      by the related tap changer model and normally is constrained to be within the range of minimum and
      maximum tap positions.
    """

    TapChanger: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.SV,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    position: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SV,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": Float,
        },
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.SV,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.SV
