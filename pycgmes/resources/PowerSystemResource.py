# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass
class PowerSystemResource(IdentifiedObject):
    """
    A power system resource (PSR) can be an item of equipment such as a switch, an equipment container containing many
      individual items of equipment such as a substation, or an organisational entity such as sub-control area.
      Power system resources can have measurements associated.

    Location: Location of this power system resource.
    Controls: The controller outputs used to actually govern a regulating device, e.g. the magnetization of a
      synchronous machine or capacitor bank breaker actuator.
    Measurements: The measurements associated with this power system resource.
    """

    # *Association not used*
    # Type M:0..1 in CIM
    # Location : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.GL, ]})

    # *Association not used*
    # Type M:0..n in CIM
    # Controls : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.OP, ]})

    # *Association not used*
    # Type M:0..n in CIM
    # Measurements : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.OP, ]})

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.GL,
            Profile.EQBD,
            Profile.EQ,
            Profile.SC,
            Profile.SSH,
            Profile.DY,
            Profile.OP,
        }
