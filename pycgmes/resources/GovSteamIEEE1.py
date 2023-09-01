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
class GovSteamIEEE1(TurbineGovernorDynamics):
    """
    IEEE steam turbine governor model. Reference: IEEE Transactions on Power Apparatus and Systems, November/December
      1973, Volume PAS-92, Number 6, Dynamic Models for Steam and Hydro Turbines in Power System Studies, page 1904.

    mwbase: Base for power values (MWbase) (> 0). Unit = MW.
    k: Governor gain (reciprocal of droop) (K) (> 0).  Typical value = 25.
    t1: Governor lag time constant (T1) (>= 0).  Typical value = 0.
    t2: Governor lead time constant (T2) (>= 0).  Typical value = 0.
    t3: Valve positioner time constant (T3) (> 0).  Typical value = 0,1.
    uo: Maximum valve opening velocity (Uo) (> 0).  Unit = PU / s.  Typical value = 1.
    uc: Maximum valve closing velocity (Uc) (< 0).  Unit = PU / s.  Typical value = -10.
    pmax: Maximum valve opening (Pmax) (> GovSteamIEEE1.pmin).  Typical value = 1.
    pmin: Minimum valve opening (Pmin) (>= 0 and < GovSteamIEEE1.pmax).  Typical value = 0.
    t4: Inlet piping/steam bowl time constant (T4) (>= 0).  Typical value = 0,3.
    k1: Fraction of HP shaft power after first boiler pass (K1).  Typical value = 0,2.
    k2: Fraction of LP shaft power after first boiler pass (K2).  Typical value = 0.
    t5: Time constant of second boiler pass (T5) (>= 0).  Typical value = 5.
    k3: Fraction of HP shaft power after second boiler pass (K3).  Typical value = 0,3.
    k4: Fraction of LP shaft power after second boiler pass (K4).  Typical value = 0.
    t6: Time constant of third boiler pass (T6) (>= 0).  Typical value = 0,5.
    k5: Fraction of HP shaft power after third boiler pass (K5).  Typical value = 0,5.
    k6: Fraction of LP shaft power after third boiler pass (K6).  Typical value = 0.
    t7: Time constant of fourth boiler pass (T7) (>= 0).  Typical value = 0.
    k7: Fraction of HP shaft power after fourth boiler pass (K7).  Typical value = 0.
    k8: Fraction of LP shaft power after fourth boiler pass (K8).  Typical value = 0.
    """

    mwbase: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k: float = Field(
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

    t2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    uo: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    uc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmax: float = Field(
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

    t4: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t5: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k4: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t6: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k5: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k6: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t7: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k7: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k8: float = Field(
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
