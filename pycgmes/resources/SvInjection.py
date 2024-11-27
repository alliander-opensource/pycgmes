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
class SvInjection(Base):
    """
    The SvInjection reports the calculated bus injection minus the sum of the terminal flows. The terminal flow is
      positive out from the bus (load sign convention) and bus injection has positive flow into the bus. SvInjection
      may have the remainder after state estimation or slack after power flow calculation.

    TopologicalNode: The topological node associated with the flow injection state variable.
    pInjection: The active power mismatch between calculated injection and initial injection.  Positive sign means
      injection into the TopologicalNode (bus).
    qInjection: The reactive power mismatch between calculated injection and initial injection.  Positive sign means
      injection into the TopologicalNode (bus).
    """

    TopologicalNode: Optional[str] = Field(
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

    pInjection: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SV,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "ActivePower",
        },
    )

    qInjection: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SV,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "ReactivePower",
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
