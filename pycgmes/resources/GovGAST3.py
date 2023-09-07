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
class GovGAST3(TurbineGovernorDynamics):
    """
    Generic turbogas with acceleration and temperature controller.

    bp: Droop (bp).  Typical value = 0,05.
    tg: Time constant of speed governor (Tg) (>= 0).  Typical value = 0,05.
    rcmx: Maximum fuel flow (RCMX).  Typical value = 1.
    rcmn: Minimum fuel flow (RCMN).  Typical value = -0,1.
    ky: Coefficient of transfer function of fuel valve positioner (Ky).  Typical value = 1.
    ty: Time constant of fuel valve positioner (Ty) (>= 0).  Typical value = 0,2.
    tac: Fuel control time constant (Tac) (>= 0).  Typical value = 0,1.
    kac: Fuel system feedback (KAC).  Typical value = 0.
    tc: Compressor discharge volume time constant (Tc) (>= 0).  Typical value = 0,2.
    bca: Acceleration limit set-point (Bca).  Unit = 1/s.  Typical value = 0,01.
    kca: Acceleration control integral gain (Kca). Unit = 1/s.  Typical value = 100.
    dtc: Exhaust temperature variation due to fuel flow increasing from 0 to 1 PU (deltaTc).  Typical value = 390.
    ka: Minimum fuel flow (Ka).  Typical value = 0,23.
    tsi: Time constant of radiation shield (Tsi) (>= 0).  Typical value = 15.
    ksi: Gain of radiation shield (Ksi).  Typical value = 0,8.
    ttc: Time constant of thermocouple (Ttc) (>= 0).  Typical value = 2,5.
    tfen: Turbine rated exhaust temperature correspondent to Pm=1 PU (Tfen).  Typical value = 540.
    td: Temperature controller derivative gain (Td) (>= 0).  Typical value = 3,3.
    tt: Temperature controller integration rate (Tt).  Typical value = 250.
    mxef: Fuel flow maximum positive error value (MXef).  Typical value = 0,05.
    mnef: Fuel flow maximum negative error value (MNef).  Typical value = -0,05.
    """

    bp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tg: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rcmx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rcmn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ky: float = Field(
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

    tac: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kac: float = Field(
        default=0.0,
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

    bca: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kca: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dtc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ka: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tsi: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ksi: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ttc: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tfen: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    td: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tt: float = Field(
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
