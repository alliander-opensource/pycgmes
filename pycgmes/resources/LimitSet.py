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
class LimitSet(IdentifiedObject):
    """
    Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets
      corresponding to seasonal or other changing conditions. The condition is captured in the name and description
      attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used
      this way.

    isPercentageLimits: Tells if the limit values are in percentage of normalValue or the specified Unit for
      Measurements and Controls.
    """

    isPercentageLimits: bool = Field(
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
