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
class WindGenType4IEC(IdentifiedObject):
    """
    IEC type 4 generator set model. Reference: IEC 61400-27-1:2015, 5.6.3.4.

    WindTurbineType4aIEC: Wind turbine type 4A model with which this wind generator type 4 model is associated.
    WindTurbineType4bIEC: Wind turbine type 4B model with which this wind generator type 4 model is associated.
    dipmax: Maximum active current ramp rate (dipmax). It is a project-dependent parameter.
    diqmax: Maximum reactive current ramp rate (diqmax). It is a project-dependent parameter.
    diqmin: Minimum reactive current ramp rate (diqmin). It is a project-dependent parameter.
    tg: Time constant (Tg) (>= 0). It is a type-dependent parameter.
    """

    WindTurbineType4aIEC: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": False,
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    WindTurbineType4bIEC: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": False,
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    dipmax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "PU",
        },
    )

    diqmax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "PU",
        },
    )

    diqmin: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "PU",
        },
    )

    tg: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "Seconds",
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
