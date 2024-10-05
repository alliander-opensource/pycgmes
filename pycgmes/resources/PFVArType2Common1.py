"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .PFVArControllerType2Dynamics import PFVArControllerType2Dynamics


@dataclass
class PFVArType2Common1(PFVArControllerType2Dynamics):
    """
    Power factor / reactive power regulator. This model represents the power factor or reactive power controller such as
      the Basler SCP-250. The controller measures power factor or reactive power (PU on generator rated power) and
      compares it with the operator's set point. [Footnote: Basler SCP-250 is an example of a suitable product
      available commercially. This information is given for the convenience of users of this document and does not
      constitute an endorsement by IEC of this product.]

    j: Selector (J). true = control mode for reactive power false = control mode for power factor.
    ki: Reset gain (Ki).
    kp: Proportional gain (Kp).
    max: Output limit (max).
    ref: Reference value of reactive power or power factor (Ref). The reference value is initialised by this model. This
      initialisation can override the value exchanged by this attribute to represent a plant operator`s change
      of the reference setting.
    """

    j: bool = Field(
        default=False,
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

    ki: float = Field(
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

    kp: float = Field(
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

    max: float = Field(
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

    ref: float = Field(
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
