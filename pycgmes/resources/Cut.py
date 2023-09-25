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
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .Switch import Switch


@dataclass(config=DataclassConfig)
class Cut(Switch):
    """
    A cut separates a line segment into two parts. The cut appears as a switch inserted between these two parts and
      connects them together. As the cut is normally open there is no galvanic connection between the two line
      segment parts. But it is possible to close the cut to get galvanic connection. The cut terminals are oriented
      towards the line segment terminals with the same sequence number. Hence the cut terminal with sequence number
      equal to 1 is oriented to the line segment's terminal with sequence number equal to 1. The cut terminals also
      act as connection points for jumpers and other equipment, e.g. a mobile generator. To enable this,
      connectivity nodes are placed at the cut terminals. Once the connectivity nodes are in place any conducting
      equipment can be connected at them.

    ACLineSegment: The line segment to which the cut is applied.
    lengthFromTerminal1: The length to the place where the cut is located starting from side one of the cut line
      segment, i.e. the line segment Terminal with sequenceNumber equal to 1.
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
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
