# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class PhaseCode(Base):
    """
    An unordered enumeration of phase identifiers.  Allows designation of phases for both transmission and distribution
      equipment, circuits and loads.   The enumeration, by itself, does not describe how the phases are connected
      together or connected to ground.  Ground is not explicitly denoted as a phase. Residential and small
      commercial loads are often served from single-phase, or split-phase, secondary circuits. For the example of
      s12N, phases 1 and 2 refer to hot wires that are 180 degrees out of phase, while N refers to the neutral wire.
      Through single-phase transformer connections, these secondary circuits may be served from one or two of the
      primary phases A, B, and C. For three-phase loads, use the A, B, C phase codes instead of s12N. The integer
      values are from IEC 61968-9 to support revenue metering applications.

    """

    # No attributes defined for this class.

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.OP,
        }
