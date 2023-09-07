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
from .RegulatingCondEq import RegulatingCondEq


@dataclass(config=DataclassConfig)
class RotatingMachine(RegulatingCondEq):
    """
    A rotating machine which may be used as a generator or motor.

    GeneratingUnit: A synchronous machine may operate as a generator and as such becomes a member of a generating unit.
    HydroPump: The synchronous machine drives the turbine which moves the water from a low elevation to a higher
      elevation. The direction of machine rotation for pumping may or may not be the same as for
      generating.
    ratedPowerFactor: Power factor (nameplate data). It is primarily used for short circuit data exchange according to
      IEC 60909. The attribute cannot be a negative value.
    ratedS: Nameplate apparent power rating for the unit. The attribute shall have a positive value.
    ratedU: Rated voltage (nameplate data, Ur in IEC 60909-0). It is primarily used for short circuit data exchange
      according to IEC 60909. The attribute shall be a positive value.
    p: Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting
      value for a steady state solution.
    q: Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting
      value for a steady state solution.
    """

    GeneratingUnit: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # HydroPump : Optional[str] = Field(default=None, in_profiles = [Profile.EQ, ])

    ratedPowerFactor: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    ratedS: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    ratedU: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    p: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    q: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
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
            Profile.SC,
            Profile.SSH,
            Profile.DY,
        }
