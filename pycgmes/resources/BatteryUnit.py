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
from .PowerElectronicsUnit import PowerElectronicsUnit


@dataclass
class BatteryUnit(PowerElectronicsUnit):
    """
    An electrochemical energy storage device.

    ratedE: Full energy storage capacity of the battery. The attribute shall be a positive value.
    batteryState: The current state of the battery (charging, full, etc.).
    storedE: Amount of energy currently stored. The attribute shall be a positive value or zero and lower than
      BatteryUnit.ratedE.
    """

    ratedE: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
    )

    batteryState: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.SSH,
            ]
        },
    )

    storedE: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SSH,
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
