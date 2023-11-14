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
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovHydroWPID(TurbineGovernorDynamics):
    """
    WoodwardTM PID hydro governor. [Footnote: Woodward PID hydro governors are an example of suitable products available
      commercially. This information is given for the convenience of users of this document and does not constitute
      an endorsement by IEC of these products.]

    mwbase: Base for power values  (MWbase) (> 0).  Unit = MW.
    treg: Speed detector time constant (Treg) (>= 0).
    reg: Permanent drop (Reg).
    kp: Proportional gain (Kp).  Typical value = 0,1.
    ki: Reset gain (Ki).  Typical value = 0,36.
    kd: Derivative gain (Kd).  Typical value = 1,11.
    ta: Controller time constant (Ta) (>= 0).  Typical value = 0.
    tb: Gate servo time constant (Tb) (>= 0).  Typical value = 0.
    velmax: Maximum gate opening velocity (Velmax) (> GovHydroWPID.velmin).  Unit = PU / s.  Typical value = 0.
    velmin: Maximum gate closing velocity (Velmin) (< GovHydroWPID.velmax).  Unit = PU / s.  Typical value = 0.
    gatmax: Gate opening limit maximum (Gatmax) (> GovHydroWPID.gatmin).
    gatmin: Gate opening limit minimum (Gatmin) (< GovHydroWPID.gatmax).
    tw: Water inertia time constant (Tw) (>= 0).  Typical value = 0.
    pmax: Maximum power output (Pmax) (> GovHydroWPID.pmin).
    pmin: Minimum power output (Pmin) (< GovHydroWPID.pmax).
    d: Turbine damping factor (D).  Unit = delta P / delta speed.
    gv3: Gate position 3 (Gv3) (= 1,0).
    gv1: Gate position 1 (Gv1).
    pgv1: Output at Gv1 PU of MWbase (Pgv1).
    gv2: Gate position 2 (Gv2).
    pgv2: Output at Gv2 PU of MWbase (Pgv2).
    pgv3: Output at Gv3 PU of MWbase (Pgv3).
    """

    mwbase: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    treg: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    reg: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ki: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kd: float = Field(
        default=0.0,
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

    tb: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    velmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    velmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gatmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gatmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tw: int = Field(
        default=0,
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

    d: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gv3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gv1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pgv1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gv2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pgv2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pgv3: float = Field(
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
