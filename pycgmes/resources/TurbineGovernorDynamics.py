"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass
class TurbineGovernorDynamics(DynamicsFunctionBlock):
    """
    Turbine-governor function block whose behaviour is described by reference to a standard model or by definition of a
      user-defined model.

    AsynchronousMachineDynamics: Asynchronous machine model with which this turbine-governor model is associated.
      TurbineGovernorDynamics shall have either an association to
      SynchronousMachineDynamics or to AsynchronousMachineDynamics.
    SynchronousMachineDynamics: Synchronous machine model with which this turbine-governor model is associated.
      TurbineGovernorDynamics shall have either an association to
      SynchronousMachineDynamics or to AsynchronousMachineDynamics.
    TurbineLoadControllerDynamics: Turbine load controller providing input to this turbine-governor.
    """

    AsynchronousMachineDynamics: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    SynchronousMachineDynamics: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    TurbineLoadControllerDynamics: Optional[str] = Field(
        default=None,
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
