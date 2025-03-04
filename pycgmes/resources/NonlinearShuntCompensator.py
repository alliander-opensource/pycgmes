"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .ShuntCompensator import ShuntCompensator


@dataclass
class NonlinearShuntCompensator(ShuntCompensator):
    """
    A non linear shunt compensator has bank or section admittance values that differ. The attributes g, b, g0 and b0 of
      the associated NonlinearShuntCompensatorPoint describe the total conductance and admittance of a
      NonlinearShuntCompensatorPoint at a section number specified by NonlinearShuntCompensatorPoint.sectionNumber.

    NonlinearShuntCompensatorPoints: All points of the non-linear shunt compensator.
    """

    NonlinearShuntCompensatorPoints: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
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
            Profile.EQ,
            Profile.SSH,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
