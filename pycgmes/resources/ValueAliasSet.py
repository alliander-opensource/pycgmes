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
class ValueAliasSet(IdentifiedObject):
    """
    Describes the translation of a set of values into a name and is intendend to facilitate custom translations. Each
      ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open,
      Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g.
      0->"Invalid", 1->"Open", 2->"Closed", 3->"Intermediate". Each ValueToAlias member in ValueAliasSet.Value
      describe a mapping for one particular value to a name.

    Commands: The Commands using the set for translation.
    Discretes: The Measurements using the set for translation.
    RaiseLowerCommands: The Commands using the set for translation.
    Values: The ValueToAlias mappings included in the set.
    """

    Commands: list = Field(
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

    Discretes: list = Field(
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

    RaiseLowerCommands: list = Field(
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

    Values: list = Field(
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
            Profile.OP,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.OP
