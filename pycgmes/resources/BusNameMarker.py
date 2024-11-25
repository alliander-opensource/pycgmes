"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .IdentifiedObject import IdentifiedObject
from .Integer import Integer


@dataclass
class BusNameMarker(IdentifiedObject):
    """
    Used to apply user standard names to TopologicalNodes. Associated with one or more terminals that are normally
      connected with the bus name.    The associated terminals are normally connected by non-retained switches. For
      a ring bus station configuration, all BusbarSection terminals in the ring are typically associated.   For a
      breaker and a half scheme, both BusbarSections would normally be associated.  For a ring bus, all
      BusbarSections would normally be associated.  For a "straight" busbar configuration, normally only the main
      terminal at the BusbarSection would be associated.

    ReportingGroup: The reporting group to which this bus name marker belongs.
    Terminal: The terminals associated with this bus name marker.
    priority: Priority of bus name marker for use as topology bus name.  Use 0 for do not care.  Use 1 for highest
      priority.  Use 2 as priority is less than 1 and so on.
    """

    ReportingGroup: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    Terminal: list = Field(
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

    priority: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": Integer,
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
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
