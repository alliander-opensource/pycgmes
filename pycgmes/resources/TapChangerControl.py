# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .RegulatingControl import RegulatingControl


@dataclass
class TapChangerControl(RegulatingControl):
    """
    Describes behaviour specific to tap changers, e.g. how the voltage at the end of a line varies with the load level
      and compensation of the voltage drop by tap adjustment.

    TapChanger: The tap changers that participates in this regulating tap control scheme.
    """

    # *Association not used*
    # Type M:1..n in CIM
    # TapChanger : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]})

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
