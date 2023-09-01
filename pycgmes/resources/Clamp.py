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
from .ConductingEquipment import ConductingEquipment


@dataclass(config=DataclassConfig)
class Clamp(ConductingEquipment):
    """
    A Clamp is a galvanic connection at a line segment where other equipment is connected. A Clamp does not cut the line
      segment.  A Clamp is ConductingEquipment and has one Terminal with an associated ConnectivityNode. Any other
      ConductingEquipment can be connected to the Clamp ConnectivityNode.

    ACLineSegment: The line segment to which the clamp is connected.
    lengthFromTerminal1: The length to the place where the clamp is located starting from side one of the line segment,
      i.e. the line segment terminal with sequence number equal to 1.
    """

    ACLineSegment: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    lengthFromTerminal1: float = Field(
        default=0.0,
        in_profiles=[
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
            Profile.EQ,
        }
