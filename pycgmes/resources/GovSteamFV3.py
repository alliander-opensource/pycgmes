# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass
class GovSteamFV3(TurbineGovernorDynamics):
    """
    Simplified GovSteamIEEE1 steam turbine governor with Prmax limit and fast valving.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    k: Governor gain, (reciprocal of droop) (K).  Typical value = 20.
    t1: Governor lead time constant (T1) (>= 0).  Typical value = 0.
    t2: Governor lag time constant (T2) (>= 0).  Typical value = 0.
    t3: Valve positioner time constant (T3) (> 0).  Typical value = 0.
    uo: Maximum valve opening velocity (Uo).  Unit = PU / s.  Typical value = 0,1.
    uc: Maximum valve closing velocity (Uc).  Unit = PU / s.  Typical value = -1.
    pmax: Maximum valve opening, PU of MWbase (Pmax) (> GovSteamFV3.pmin).  Typical value = 1.
    pmin: Minimum valve opening, PU of MWbase (Pmin) (< GovSteamFV3.pmax).  Typical value = 0.
    t4: Inlet piping/steam bowl time constant (T4) (>= 0).  Typical value = 0,2.
    k1: Fraction of turbine power developed after first boiler pass (K1).  Typical value = 0,2.
    t5: Time constant of second boiler pass (i.e. reheater) (T5) (> 0 if fast valving is used, otherwise >= 0).  Typical
      value = 0,5.
    k2: Fraction of turbine power developed after second boiler pass (K2).  Typical value = 0,2.
    t6: Time constant of crossover or third boiler pass (T6) (>= 0).  Typical value = 10.
    k3: Fraction of hp turbine power developed after crossover or third boiler pass (K3). Typical value = 0,6.
    ta: Time to close intercept valve (IV) (Ta) (>= 0).  Typical value = 0,97.
    tb: Time until IV starts to reopen (Tb) (>= 0).  Typical value = 0,98.
    tc: Time until IV is fully open (Tc) (>= 0).  Typical value = 0,99.
    prmax: Max. pressure in reheater (Prmax).  Typical value = 1.
    gv1: Nonlinear gain valve position point 1 (GV1).  Typical value = 0.
    pgv1: Nonlinear gain power value point 1 (Pgv1).  Typical value = 0.
    gv2: Nonlinear gain valve position point 2 (GV2).  Typical value = 0,4.
    pgv2: Nonlinear gain power value point 2 (Pgv2).  Typical value = 0,75.
    gv3: Nonlinear gain valve position point 3 (GV3).  Typical value = 0,5.
    pgv3: Nonlinear gain power value point 3 (Pgv3).  Typical value = 0,91.
    gv4: Nonlinear gain valve position point 4 (GV4).  Typical value = 0,6.
    pgv4: Nonlinear gain power value point 4 (Pgv4).  Typical value = 0,98.
    gv5: Nonlinear gain valve position point 5 (GV5).  Typical value = 1.
    pgv5: Nonlinear gain power value point 5 (Pgv5).  Typical value = 1.
    gv6: Nonlinear gain valve position point 6 (GV6).  Typical value = 0.
    pgv6: Nonlinear gain power value point 6 (Pgv6).  Typical value = 0.
    """

    mwbase: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    k: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t1: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t2: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t3: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    uo: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    uc: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    pmax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    pmin: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t4: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    k1: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t5: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    k2: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t6: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    k3: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ta: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tb: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tc: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    prmax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    gv1: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    pgv1: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    gv2: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    pgv2: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    gv3: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    pgv3: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    gv4: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    pgv4: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    gv5: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    pgv5: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    gv6: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    pgv6: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
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
