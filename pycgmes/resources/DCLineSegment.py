# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile
from .DCConductingEquipment import DCConductingEquipment


@dataclass(config=DataclassConfig)
class DCLineSegment(DCConductingEquipment):
    """
    A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to
      carry direct current between points in the DC region of the power system.

    capacitance: Capacitance of the DC line segment. Significant for cables only.
    inductance: Inductance of the DC line segment. Negligible compared with DCSeriesDevice used for smoothing.
    resistance: Resistance of the DC line segment.
    length: Segment length for calculating line section capabilities.
    """

    capacitance: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    inductance: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    resistance: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    length: float = Field(
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
