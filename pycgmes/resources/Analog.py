"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .Measurement import Measurement


@dataclass
class Analog(Measurement):
    """
    Analog represents an analog Measurement.

    AnalogValues: The values connected to this measurement.
    LimitSets: A measurement may have zero or more limit ranges defined for it.
    positiveFlowIn: If true then this measurement is an active power, reactive power or current with the convention that
      a positive value measured at the Terminal means power is flowing into the related
      PowerSystemResource.
    """

    AnalogValues: list = Field(
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

    LimitSets: list = Field(
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

    positiveFlowIn: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.OP
