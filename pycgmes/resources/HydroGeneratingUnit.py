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

from .GeneratingUnit import GeneratingUnit


@dataclass(config=DataclassConfig)
class HydroGeneratingUnit(GeneratingUnit):
    """
    A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan).

    energyConversionCapability: Energy conversion capability for generating.
    dropHeight: The height water drops from the reservoir mid-point to the turbine.
    turbineType: Type of turbine.
    HydroPowerPlant: The hydro generating unit belongs to a hydro power plant.
    """

    energyConversionCapability: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    dropHeight: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    turbineType: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    HydroPowerPlant: Optional[str] = Field(
        default=None,
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
            Profile.SSH,
        }
