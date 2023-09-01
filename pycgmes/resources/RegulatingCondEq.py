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
from .EnergyConnection import EnergyConnection


@dataclass(config=DataclassConfig)
class RegulatingCondEq(EnergyConnection):
    """
    A type of conducting equipment that can regulate a quantity (i.e. voltage or flow) at a specific point in the
      network.

    RegulatingControl: The regulating control scheme in which this equipment participates.
    controlEnabled: Specifies the regulation status of the equipment.  True is regulating, false is not regulating.
    """

    RegulatingControl: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    controlEnabled: bool = Field(
        default=False,
        in_profiles=[
            Profile.SSH,
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
            Profile.SSH,
            Profile.DY,
        }
