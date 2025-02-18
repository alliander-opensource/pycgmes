"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .WindTurbineType1or2Dynamics import WindTurbineType1or2Dynamics


@dataclass
class WindTurbineType1or2IEC(WindTurbineType1or2Dynamics):
    """
    Parent class supporting relationships to IEC wind turbines type 1 and type 2 including their control models.
      Generator model for wind turbine of IEC type 1 or type 2 is a standard asynchronous generator model.
      Reference: IEC 61400-27-1:2015, 5.5.2 and 5.5.3.

    WindMechIEC: Wind mechanical model associated with this wind generator type 1 or type 2 model.
    WindProtectionIEC: Wind turbune protection model associated with this wind generator type 1 or type 2 model.
    """

    WindMechIEC: Optional[str] = Field(
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

    WindProtectionIEC: Optional[str] = Field(
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
