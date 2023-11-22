# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .PowerSystemResource import PowerSystemResource


@dataclass
class CogenerationPlant(PowerSystemResource):
    """
    A set of thermal generating units for the production of electrical energy and process steam (usually from the output
      of the steam turbines). The steam sendout is typically used for industrial purposes or for municipal heating
      and cooling.

    ThermalGeneratingUnits: A thermal generating unit may be a member of a cogeneration plant.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # ThermalGeneratingUnits : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
