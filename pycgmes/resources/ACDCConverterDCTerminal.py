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
from .Base import DataclassConfig, Profile
from .DCBaseTerminal import DCBaseTerminal


@dataclass(config=DataclassConfig)
class ACDCConverterDCTerminal(DCBaseTerminal):
    """
    A DC electrical connection point at the AC/DC converter. The AC/DC converter is electrically connected also to the
      AC side. The AC connection is inherited from the AC conducting equipment in the same way as any other AC
      equipment. The AC/DC converter DC terminal is separate from generic DC terminal to restrict the connection
      with the AC side to AC/DC converter and so that no other DC conducting equipment can be connected to the AC
      side.

    DCConductingEquipment: A DC converter terminal belong to an DC converter.
    polarity: Represents the normal network polarity condition. Depending on the converter configuration the value shall
      be set as follows: - For a monopole with two converter terminals use DCPolarityKind `positive` and
      `negative`. - For a bi-pole or symmetric monopole with three converter terminals use DCPolarityKind
      `positive`, `middle` and `negative`.
    """

    DCConductingEquipment: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    polarity: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.EQ,
            Profile.SSH,
        }
