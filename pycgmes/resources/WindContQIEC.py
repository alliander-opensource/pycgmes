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

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindContQIEC(IdentifiedObject):
    """
    Q control model. Reference: IEC 61400-27-1:2015, 5.6.5.7.

    iqh1: Maximum reactive current injection during dip (iqh1). It is a type-dependent parameter.
    iqmax: Maximum reactive current injection (iqmax) (> WindContQIEC.iqmin). It is a type-dependent parameter.
    iqmin: Minimum reactive current injection (iqmin) (< WindContQIEC.iqmax). It is a type-dependent parameter.
    iqpost: Post fault reactive current injection (iqpost). It is a project-dependent parameter.
    kiq: Reactive power PI controller integration gain (KI,q). It is a type-dependent parameter.
    kiu: Voltage PI controller integration gain (KI,u). It is a type-dependent parameter.
    kpq: Reactive power PI controller proportional gain (KP,q). It is a type-dependent parameter.
    kpu: Voltage PI controller proportional gain (KP,u). It is a type-dependent parameter.
    kqv: Voltage scaling factor for UVRT current (Kqv). It is a project-dependent parameter.
    tpfiltq: Power measurement filter time constant (Tpfiltq) (>= 0). It is a type-dependent parameter.
    rdroop: Resistive component of voltage drop impedance (rdroop) (>= 0). It is a project-dependent parameter.
    tufiltq: Voltage measurement filter time constant (Tufiltq) (>= 0). It is a type-dependent parameter.
    tpost: Length of time period where post fault reactive power is injected (Tpost) (>= 0). It is a project-dependent
      parameter.
    tqord: Time constant in reactive power order lag (Tqord) (>= 0). It is a type-dependent parameter.
    udb1: Voltage deadband lower limit (udb1). It is a type-dependent parameter.
    udb2: Voltage deadband upper limit (udb2). It is a type-dependent parameter.
    umax: Maximum voltage in voltage PI controller integral term (umax) (> WindContQIEC.umin). It is a type-dependent
      parameter.
    umin: Minimum voltage in voltage PI controller integral term (umin) (< WindContQIEC.umax). It is a type-dependent
      parameter.
    uqdip: Voltage threshold for UVRT detection in Q control (uqdip). It is a type-dependent parameter.
    uref0: User-defined bias in voltage reference (uref0). It is a case-dependent parameter.
    windQcontrolModesType: Types of general wind turbine Q control modes (MqG).  It is a project-dependent parameter.
    windUVRTQcontrolModesType: Types of UVRT Q control modes (MqUVRT). It is a project-dependent parameter.
    xdroop: Inductive component of voltage drop impedance (xdroop) (>= 0). It is a project-dependent parameter.
    WindTurbineType3or4IEC: Wind turbine type 3 or type 4 model with which this reactive control model is associated.
    """

    iqh1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    iqmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    iqmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    iqpost: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kiq: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kiu: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kpq: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kpu: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kqv: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tpfiltq: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rdroop: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tufiltq: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tpost: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tqord: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    udb1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    udb2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    umax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    umin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    uqdip: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    uref0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    windQcontrolModesType: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    windUVRTQcontrolModesType: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    xdroop: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType3or4IEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
