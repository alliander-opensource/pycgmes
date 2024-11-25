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
class DCTopologicalIsland(IdentifiedObject):
    """
    An electrically connected subset of the network. DC topological islands can change as the current network state
      changes, e.g. due to:  - disconnect switches or breakers changing state in a SCADA/EMS. - manual creation,
      change or deletion of topological nodes in a planning tool. Only energised TopologicalNode-s shall be part of
      the topological island.

    DCTopologicalNodes: The DC topological nodes in a DC topological island.
    """

    DCTopologicalNodes: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.SV,
            ],
            "is_used": True,
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
            Profile.SV,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.SV
