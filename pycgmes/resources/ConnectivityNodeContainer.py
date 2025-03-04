"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .PowerSystemResource import PowerSystemResource


@dataclass
class ConnectivityNodeContainer(PowerSystemResource):
    """
    A base class for all objects that may contain connectivity nodes or topological nodes.

    ConnectivityNodes: Connectivity nodes which belong to this connectivity node container.
    TopologicalNode: The topological nodes which belong to this connectivity node container.
    """

    ConnectivityNodes: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
                Profile.EQBD,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    TopologicalNode: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.TP,
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
            Profile.EQBD,
            Profile.TP,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
