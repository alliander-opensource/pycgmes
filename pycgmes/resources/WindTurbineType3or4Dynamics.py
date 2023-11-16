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
from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass
class WindTurbineType3or4Dynamics(DynamicsFunctionBlock):
    """
    Parent class supporting relationships to wind turbines type 3 and type 4 and wind plant including their control
      models.

    PowerElectronicsConnection: The power electronics connection associated with this wind turbine type 3 or type 4
      dynamics model.
    RemoteInputSignal: Remote input signal used by these wind turbine type 3 or type 4 models.
    WindPlantDynamics: The wind plant with which the wind turbines type 3 or type 4 are associated.
    """

    PowerElectronicsConnection: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    RemoteInputSignal: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    WindPlantDynamics: Optional[str] = Field(
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
