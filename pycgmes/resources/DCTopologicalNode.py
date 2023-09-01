# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class DCTopologicalNode(IdentifiedObject):
    """
    DC bus.

    DCTerminals: See association end TopologicalNode.Terminal.
    DCEquipmentContainer: The connectivity node container to which the topological node belongs.
    DCNodes: The DC connectivity nodes combined together to form this DC topological node.  May depend on the current
      state of switches in the network.
    DCTopologicalIsland: A DC topological node belongs to a DC topological island.
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # DCTerminals : list = Field(default_factory=list, in_profiles = [Profile.TP, ])

    DCEquipmentContainer: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.TP,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # DCNodes : list = Field(default_factory=list, in_profiles = [Profile.TP, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # DCTopologicalIsland : Optional[str] = Field(default=None, in_profiles = [Profile.SV, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.SV,
        }
