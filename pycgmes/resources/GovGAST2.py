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
class GovGAST2(TurbineGovernorDynamics):
    """
    Gas turbine.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    w: Governor gain (1/droop) on turbine rating (W).
    x: Governor lead time constant (X) (>= 0).
    y: Governor lag time constant (Y) (> 0).
    z: Governor mode (Z). 1 = droop 0 = isochronous.
    etd: Turbine and exhaust delay (Etd) (>= 0).
    tcd: Compressor discharge time constant (Tcd) (>= 0).
    trate: Turbine rating (Trate).  Unit = MW.
    t: Fuel control time constant (T) (>= 0).
    tmax: Maximum turbine limit (Tmax) (> GovGAST2.tmin).
    tmin: Minimum turbine limit (Tmin) (< GovGAST2.tmax).
    ecr: Combustion reaction time delay (Ecr) (>= 0).
    k3: Ratio of fuel adjustment (K3).
    a: Valve positioner (A).
    b: Valve positioner (B).
    c: Valve positioner (C).
    tf: Fuel system time constant (Tf) (>= 0).
    kf: Fuel system feedback (Kf).
    k5: Gain of radiation shield (K5).
    k4: Gain of radiation shield (K4).
    t3: Radiation shield time constant (T3) (>= 0).
    t4: Thermocouple time constant (T4) (>= 0).
    tt: Temperature controller integration rate (Tt) (>= 0).
    t5: Temperature control time constant (T5) (>= 0).
    af1: Exhaust temperature parameter (Af1).  Unit = PU temperature.  Based on temperature in degrees C.
    bf1: (Bf1).  Bf1 = E(1 - W) where E (speed sensitivity coefficient) is 0,55 to 0,65 x Tr.  Unit = PU temperature.
      Based on temperature in degrees C.
    af2: Coefficient equal to 0,5(1-speed) (Af2).
    bf2: Turbine torque coefficient Khhv (depends on heating value of fuel stream in combustion chamber) (Bf2).
    cf2: Coefficient defining fuel flow where power output is 0% (Cf2).  Synchronous but no output.  Typically 0,23 x
      Khhv (23% fuel flow).
    tr: Rated temperature (Tr).  Unit = [SYMBOL REMOVED]C depending on parameters Af1 and Bf1.
    k6: Minimum fuel flow (K6).
    tc: Temperature control (Tc).  Unit = [SYMBOL REMOVED]F or [SYMBOL REMOVED]C depending on parameters Af1 and Bf1.
    """

    mwbase: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    w: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    x: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    y: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    z: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    etd: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tcd: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    trate: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ecr: int = Field(
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

    a: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    b: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    c: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tf: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kf: float = Field(
        default=0.0,
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

    k4: float = Field(
        default=0.0,
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

    t4: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tt: int = Field(
        default=0,
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

    af1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    bf1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    af2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    bf2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    cf2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tr: float = Field(
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

    tc: float = Field(
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
