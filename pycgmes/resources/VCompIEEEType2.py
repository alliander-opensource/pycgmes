"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .VoltageCompensatorDynamics import VoltageCompensatorDynamics


@dataclass
class VCompIEEEType2(VoltageCompensatorDynamics):
    """
    Terminal voltage transducer and load compensator as defined in IEEE 421.5-2005, 4. This model is designed to cover
      the following types of compensation:   reactive droop; transformer-drop or line-drop compensation; reactive
      differential compensation known also as cross-current compensation.  Reference: IEEE 421.5-2005, 4.

    GenICompensationForGenJ: Compensation of this voltage compensator`s generator for current flow out of another
      generator.
    tr: Time constant which is used for the combined voltage sensing and compensation signal (Tr) (>= 0).
    """

    GenICompensationForGenJ: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": False,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    tr: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
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
            Profile.DY,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.DY
