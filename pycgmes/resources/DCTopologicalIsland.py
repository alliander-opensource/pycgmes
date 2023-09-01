# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
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
        in_profiles=[
            Profile.SV,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.SV,
        }
