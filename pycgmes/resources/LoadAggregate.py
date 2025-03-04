"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .LoadDynamics import LoadDynamics


@dataclass
class LoadAggregate(LoadDynamics):
    """
    Aggregate loads are used to represent all or part of the real and reactive load from one or more loads in the static
      (power flow) data. This load is usually the aggregation of many individual load devices and the load model is
      an approximate representation of the aggregate response of the load devices to system disturbances. Standard
      aggregate load model comprised of static and/or dynamic components.  A static load model represents the
      sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus
      voltage. A dynamic load model can be used to represent the aggregate response of the motor components of the
      load.

    LoadMotor: Aggregate motor (dynamic) load associated with this aggregate load.
    LoadStatic: Aggregate static load associated with this aggregate load.
    """

    LoadMotor: Optional[str] = Field(
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

    LoadStatic: Optional[str] = Field(
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
