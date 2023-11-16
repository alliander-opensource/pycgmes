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
from .GeneratingUnit import GeneratingUnit


@dataclass
class WindGeneratingUnit(GeneratingUnit):
    """
    A wind driven generating unit, connected to the grid by means of a rotating machine.  May be used to represent a
      single turbine or an aggregation.

    windGenUnitType: The kind of wind generating unit.
    WindPowerPlant: A wind power plant may have wind generating units.
    """

    windGenUnitType: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
    )

    WindPowerPlant: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SSH,
        }
