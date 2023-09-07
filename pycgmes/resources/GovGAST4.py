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
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovGAST4(TurbineGovernorDynamics):
    """
    Generic turbogas.

    bp: Droop (bp).  Typical value = 0,05.
    ty: Time constant of fuel valve positioner (Ty) (>= 0).  Typical value = 0,1.
    ta: Maximum gate opening velocity (TA) (>= 0).  Typical value = 3.
    tc: Maximum gate closing velocity (TC) (>= 0).  Typical value = 0,5.
    tcm: Fuel control time constant (Tcm) (>= 0).  Typical value = 0,1.
    ktm: Compressor gain (Ktm).  Typical value = 0.
    tm: Compressor discharge volume time constant (Tm) (>= 0).  Typical value = 0,2.
    rymx: Maximum valve opening (RYMX).  Typical value = 1,1.
    rymn: Minimum valve opening (RYMN).  Typical value = 0.
    mxef: Fuel flow maximum positive error value (MXef).  Typical value = 0,05.
    mnef: Fuel flow maximum negative error value (MNef).  Typical value = -0,05.
    """

    bp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ty: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ta: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tc: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tcm: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ktm: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tm: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rymx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rymn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    mxef: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    mnef: float = Field(
        default=0.0,
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
