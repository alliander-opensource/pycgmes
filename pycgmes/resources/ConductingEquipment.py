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

from .Equipment import Equipment


@dataclass(config=DataclassConfig)
class ConductingEquipment(Equipment):
    """
    The parts of the AC power system that are designed to carry current or that are conductively connected through
      terminals.

    Terminals: Conducting equipment have terminals that may be connected to other conducting equipment terminals via
      connectivity nodes or topological nodes.
    BaseVoltage: Base voltage of this conducting equipment.  Use only when there is no voltage level container used and
      only one base voltage applies.  For example, not used for transformers.
    SvStatus: The status state variable associated with this conducting equipment.
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Terminals : list = Field(default_factory=list, in_profiles = [Profile.EQBD, Profile.EQ, Profile.DY, ]) # noqa: E501

    BaseVoltage: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # SvStatus : Optional[str] = Field(default=None, in_profiles = [Profile.SV, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQBD,
            Profile.EQ,
            Profile.SC,
            Profile.SV,
            Profile.SSH,
            Profile.DY,
        }
