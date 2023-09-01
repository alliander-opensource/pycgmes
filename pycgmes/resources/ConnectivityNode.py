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
class ConnectivityNode(IdentifiedObject):
    """
    Connectivity nodes are points where terminals of AC conducting equipment are connected together with zero impedance.

    TopologicalNode: The topological node to which this connectivity node is assigned.  May depend on the current state
      of switches in the network.
    BoundaryPoint: The boundary point associated with the connectivity node.
    Terminals: Terminals interconnected with zero impedance at a this connectivity node.
    ConnectivityNodeContainer: Container of this connectivity node.
    """

    TopologicalNode: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.TP,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # BoundaryPoint : Optional[str] = Field(default=None, in_profiles = [Profile.EQBD, Profile.EQ, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Terminals : list = Field(default_factory=list, in_profiles = [Profile.EQBD, Profile.EQ, ])

    ConnectivityNodeContainer: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQBD,
            Profile.EQ,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.EQBD,
            Profile.EQ,
        }
