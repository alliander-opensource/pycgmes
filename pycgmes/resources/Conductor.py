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
from .ConductingEquipment import ConductingEquipment


@dataclass(config=DataclassConfig)
class Conductor(ConductingEquipment):
    """
    Combination of conducting material with consistent electrical characteristics, building a single electrical system,
      used to carry current between points in the power system.

    length: Segment length for calculating line section capabilities.
    """

    length: float = Field(
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
            Profile.SC,
        }
