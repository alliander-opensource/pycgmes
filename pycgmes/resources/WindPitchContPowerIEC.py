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
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindPitchContPowerIEC(IdentifiedObject):
    """
    Pitch control power model. Reference: IEC 61400-27-1:2015, 5.6.5.1.

    WindDynamicsLookupTable: The wind dynamics lookup table associated with this pitch control power model.
    WindGenTurbineType1bIEC: Wind turbine type 1B model with which this pitch control power model is associated.
    WindGenTurbineType2IEC: Wind turbine type 2 model with which this pitch control power model is associated.
    dpmax: Rate limit for increasing power (dpmax) (> WindPitchContPowerIEC.dpmin). It is a type-dependent parameter.
    dpmin: Rate limit for decreasing power (dpmin) (< WindPitchContPowerIEC.dpmax). It is a type-dependent parameter.
    pmin: Minimum power setting (pmin). It is a type-dependent parameter.
    pset: If pinit < pset then power will be ramped down to pmin. It is (pset) in the IEC 61400-27-1:2015. It is a type-
      dependent parameter.
    t1: Lag time constant (T1) (>= 0). It is a type-dependent parameter.
    tr: Voltage measurement time constant (Tr) (>= 0). It is a type-dependent parameter.
    uuvrt: Dip detection threshold (uUVRT). It is a type-dependent parameter.
    """

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # WindDynamicsLookupTable : list = Field(default_factory=list, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # WindGenTurbineType1bIEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # WindGenTurbineType2IEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    dpmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dpmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pset: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tr: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    uuvrt: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
