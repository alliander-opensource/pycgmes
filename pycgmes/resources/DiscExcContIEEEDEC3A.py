# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics


@dataclass(config=DataclassConfig)
class DiscExcContIEEEDEC3A(DiscontinuousExcitationControlDynamics):
    """
    IEEE type DEC3A model. In some systems, the stabilizer output is disconnected from the regulator immediately
      following a severe fault to prevent the stabilizer from competing with action of voltage regulator during the
      first swing. Reference: IEEE 421.5-2005 12.4.

    vtmin: Terminal undervoltage comparison level (VTMIN).
    tdr: Reset time delay (TDR) (>= 0).
    """

    vtmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tdr: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
