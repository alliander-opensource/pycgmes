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
from .TurbineLoadControllerDynamics import TurbineLoadControllerDynamics


@dataclass(config=DataclassConfig)
class TurbLCFB1(TurbineLoadControllerDynamics):
    """
    Turbine load controller model developed by WECC.  This model represents a supervisory turbine load controller that
      acts to maintain turbine power at a set value by continuous adjustment of the turbine governor speed-load
      reference. This model is intended to represent slow reset 'outer loop' controllers managing the action of the
      turbine governor.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    speedReferenceGovernor: Type of turbine governor reference (Type). true = speed reference governor false = load
      reference governor. Typical value = true.
    db: Controller deadband (db).  Typical value = 0.
    emax: Maximum control error (Emax) (see parameter detail 4).  Typical value = 0,02.
    fb: Frequency bias gain (Fb).  Typical value = 0.
    kp: Proportional gain (Kp).  Typical value = 0.
    ki: Integral gain (Ki).  Typical value = 0.
    fbf: Frequency bias flag (Fbf). true = enable frequency bias false = disable frequency bias. Typical value = false.
    pbf: Power controller flag (Pbf). true = enable load controller false = disable load controller. Typical value =
      false.
    tpelec: Power transducer time constant (Tpelec) (>= 0).  Typical value = 0.
    irmax: Maximum turbine speed/load reference bias (Irmax) (see parameter detail 3).  Typical value = 0.
    pmwset: Power controller setpoint (Pmwset) (see parameter detail 1).  Unit = MW. Typical value = 0.
    """

    mwbase: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    speedReferenceGovernor: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    db: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    emax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fb: float = Field(
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

    fbf: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    pbf: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    tpelec: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    irmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmwset: float = Field(
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
