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
from .PowerSystemResource import PowerSystemResource


@dataclass
class HydroPowerPlant(PowerSystemResource):
    """
    A hydro power station which can generate or pump. When generating, the generator turbines receive water from an
      upper reservoir. When pumping, the pumps receive their water from a lower reservoir.

    HydroGeneratingUnits: The hydro generating unit belongs to a hydro power plant.
    hydroPlantStorageType: The type of hydro power plant water storage.
    HydroPumps: The hydro pump may be a member of a pumped storage plant or a pump for distributing water.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # HydroGeneratingUnits : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    hydroPlantStorageType: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
    )

    # *Association not used*
    # Type M:0..n in CIM
    # HydroPumps : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]})

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
