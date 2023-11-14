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
class GeneratingUnit(Equipment):
    """
    A single or set of synchronous machines for converting mechanical power into alternating-current power. For example,
      individual machines within a set may be defined for scheduling purposes while a single control signal is
      derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional
      GeneratingUnit corresponding to the set.

    ControlAreaGeneratingUnit: ControlArea specifications for this generating unit.
    genControlSource: The source of controls for a generating unit.  Defines the control status of the generating unit.
    governorSCD: Governor Speed Changer Droop.   This is the change in generator power output divided by the change in
      frequency normalized by the nominal power of the generator and the nominal frequency and
      expressed in percent and negated. A positive value of speed change droop provides additional
      generator output upon a drop in frequency.
    longPF: Generating unit long term economic participation factor.
    maximumAllowableSpinningReserve: Maximum allowable spinning reserve. Spinning reserve will never be considered
      greater than this value regardless of the current operating point.
    maxOperatingP: This is the maximum operating active power limit the dispatcher can enter for this unit.
    minOperatingP: This is the minimum operating active power limit the dispatcher can enter for this unit.
    nominalP: The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes
      such as the governor speed change droop (governorSCD attribute). The attribute shall be a positive
      value equal to or less than RotatingMachine.ratedS.
    ratedGrossMaxP: The unit`s gross rated maximum capacity (book value). The attribute shall be a positive value.
    ratedGrossMinP: The gross rated minimum generation level which the unit can safely operate at while delivering power
      to the transmission grid. The attribute shall be a positive value.
    ratedNetMaxP: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the
      internal plant machinery from the rated gross maximum capacity. The attribute shall be a
      positive value.
    shortPF: Generating unit short term economic participation factor.
    startupCost: The initial startup cost incurred for each start of the GeneratingUnit.
    variableCost: The variable cost component of production per unit of ActivePower.
    startupTime: Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied.
    totalEfficiency: The efficiency of the unit in converting the fuel into electrical energy.
    GrossToNetActivePowerCurves: A generating unit may have a gross active power to net active power curve, describing
      the losses and auxiliary power requirements of the unit.
    RotatingMachine: A synchronous machine may operate as a generator and as such becomes a member of a generating unit.
    normalPF: Generating unit economic participation factor.  The sum of the participation factors across generating
      units does not have to sum to one.  It is used for representing distributed slack participation
      factor. The attribute shall be a positive value or zero.
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # ControlAreaGeneratingUnit : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    genControlSource: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    governorSCD: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    longPF: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    maximumAllowableSpinningReserve: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    maxOperatingP: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    minOperatingP: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    nominalP: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    ratedGrossMaxP: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    ratedGrossMinP: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    ratedNetMaxP: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    shortPF: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    startupCost: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    variableCost: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    startupTime: int = Field(
        default=0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    totalEfficiency: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # GrossToNetActivePowerCurves : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # RotatingMachine : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    normalPF: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
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
