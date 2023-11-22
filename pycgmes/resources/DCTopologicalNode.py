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

from ..utils.profile import BaseProfile, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass
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
    # Type M:0..n in CIM
    # DCTerminals : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.TP, ]})

    DCEquipmentContainer: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.TP,
            ]
        },
    )

    # *Association not used*
    # Type M:0..n in CIM
    # DCNodes : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.TP, ]})

    # *Association not used*
    # Type M:0..1 in CIM
    # DCTopologicalIsland : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SV, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.SV,
        }
