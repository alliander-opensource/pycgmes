# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ConnectivityNodeContainer import ConnectivityNodeContainer


@dataclass(config=DataclassConfig)
class EquivalentNetwork(ConnectivityNodeContainer):
    """
    A class that groups electrical equivalents, including internal nodes, of a network that has been reduced. The
      ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The
      boundary Connectivity nodes where the equivalent connects outside itself are not contained by the equivalent.

    EquivalentEquipments: The associated reduced equivalents.
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # EquivalentEquipments : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
