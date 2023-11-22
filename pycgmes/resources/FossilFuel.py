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
from .IdentifiedObject import IdentifiedObject


@dataclass
class FossilFuel(IdentifiedObject):
    """
    The fossil fuel consumed by the non-nuclear thermal generating unit.   For example, coal, oil, gas, etc.   These are
      the specific fuels that the generating unit can consume.

    fossilFuelType: The type of fossil fuel, such as coal, oil, or gas.
    ThermalGeneratingUnit: A thermal generating unit may have one or more fossil fuels.
    """

    fossilFuelType: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
    )

    ThermalGeneratingUnit: Optional[str] = Field(
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
        }
