"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass
class PowerSystemResource(IdentifiedObject):
    """
    A power system resource (PSR) can be an item of equipment such as a switch, an equipment container containing many
      individual items of equipment such as a substation, or an organisational entity such as sub-control area.
      Power system resources can have measurements associated.

    Controls: The controller outputs used to actually govern a regulating device, e.g. the magnetization of a
      synchronous machine or capacitor bank breaker actuator.
    Location: Location of this power system resource.
    Measurements: The measurements associated with this power system resource.
    """

    Controls: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    Location: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ],
            "is_used": False,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    Measurements: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
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
            Profile.DY,
            Profile.EQ,
            Profile.EQBD,
            Profile.GL,
            Profile.OP,
            Profile.SC,
            Profile.SSH,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
