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
class WindPlantDynamics(DynamicsFunctionBlock):
    """
    Parent class supporting relationships to wind turbines type 3 and type 4 and wind plant IEC and user-defined wind
      plants including their control models.

    RemoteInputSignal: The remote signal with which this power plant is associated.
    WindTurbineType3or4Dynamics: The wind turbine type 3 or type 4 associated with this wind plant.
    """

    RemoteInputSignal: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    # *Association not used*
    # Type M:1..n in CIM
    # WindTurbineType3or4Dynamics : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
