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
from .DCEquipmentContainer import DCEquipmentContainer


@dataclass(config=DataclassConfig)
class DCConverterUnit(DCEquipmentContainer):
    """
    Indivisible operative unit comprising all equipment between the point of common coupling on the AC side and the
      point of common coupling - DC side, essentially one or more converters, together with one or more converter
      transformers, converter control equipment, essential protective and switching devices and auxiliaries, if any,
      used for conversion.

    operationMode: The operating mode of an HVDC bipole (bipolar, monopolar metallic return, etc).
    Substation: The containing substation of the DC converter unit.
    """

    operationMode: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    Substation: Optional[str] = Field(
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
            Profile.EQ,
        }
