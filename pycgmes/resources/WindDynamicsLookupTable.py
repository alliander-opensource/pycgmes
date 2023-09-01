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
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindDynamicsLookupTable(IdentifiedObject):
    """
    Look up table for the purpose of wind standard models.

    WindContCurrLimIEC: The current control limitation model with which this wind dynamics lookup table is associated.
    WindContPType3IEC: The P control type 3 model with which this wind dynamics lookup table is associated.
    WindContQPQULimIEC: The QP and QU limitation model with which this wind dynamics lookup table is associated.
    WindContRotorRIEC: The rotor resistance control model with which this wind dynamics lookup table is associated.
    input: Input value (x) for the lookup table function.
    lookupTableFunctionType: Type of the lookup table function.
    output: Output value (y) for the lookup table function.
    sequence: Sequence numbers of the pairs of the input (x) and the output (y) of the lookup table function.
    WindPlantFreqPcontrolIEC: The frequency and active power wind plant control model with which this wind dynamics
      lookup table is associated.
    WindProtectionIEC: The grid protection model with which this wind dynamics lookup table is associated.
    WindPlantReactiveControlIEC: The voltage and reactive power wind plant control model with which this wind dynamics
      lookup table is associated.
    WindGenType3bIEC: The generator type 3B model with which this wind dynamics lookup table is associated.
    WindPitchContPowerIEC: The pitch control power model with which this wind dynamics lookup table is associated.
    """

    WindContCurrLimIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindContPType3IEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindContQPQULimIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindContRotorRIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    input: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    lookupTableFunctionType: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    output: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    sequence: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindPlantFreqPcontrolIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindProtectionIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindPlantReactiveControlIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindGenType3bIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindPitchContPowerIEC: Optional[str] = Field(
        default=None,
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
