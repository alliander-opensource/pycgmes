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
from .WindPlantDynamics import WindPlantDynamics


@dataclass
class WindPlantIEC(WindPlantDynamics):
    """
    Simplified IEC type plant level model.  Reference: IEC 61400-27-1:2015, Annex D.

    WindPlantFreqPcontrolIEC: Wind plant frequency and active power control model associated with this wind plant.
    WindPlantReactiveControlIEC: Wind plant model with which this wind reactive control is associated.
    """

    WindPlantFreqPcontrolIEC: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    WindPlantReactiveControlIEC: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
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
            Profile.DY,
        }
