# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile
from .Equipment import Equipment


@dataclass(config=DataclassConfig)
class PowerElectronicsUnit(Equipment):
    """
    A generating unit or battery or aggregation that connects to the AC network using power electronics rather than
      rotating machines.

    PowerElectronicsConnection: A power electronics unit has a connection to the AC network.
    maxP: Maximum active power limit. This is the maximum (nameplate) limit for the unit.
    minP: Minimum active power limit. This is the minimum (nameplate) limit for the unit.
    """

    # *Association not used*
    # Type M:1 in CIM  # pylint: disable-next=line-too-long
    # PowerElectronicsConnection : Optional[str] = Field(default=None, in_profiles = [Profile.EQ, ])

    maxP: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    minP: float = Field(
        default=0.0,
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
