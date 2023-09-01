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
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindContPType3IEC(IdentifiedObject):
    """
    P control model type 3. Reference: IEC 61400-27-1:2015, 5.6.5.4.

    dpmax: Maximum wind turbine power ramp rate (dpmax). It is a type-dependent parameter.
    dprefmax: Maximum ramp rate of wind turbine reference power (dprefmax). It is a project-dependent parameter.
    dprefmin: Minimum ramp rate of wind turbine reference power (dprefmin). It is a project-dependent parameter.
    dthetamax: Ramp limitation of torque, required in some grid codes (dtmax). It is a project-dependent parameter.
    dthetamaxuvrt: Limitation of torque rise rate during UVRT (dthetamaxUVRT). It is a project-dependent parameter.
    kdtd: Gain for active drive train damping (KDTD). It is a type-dependent parameter.
    kip: PI controller integration parameter (KIp). It is a type-dependent parameter.
    kpp: PI controller proportional gain (KPp). It is a type-dependent parameter.
    mpuvrt: Enable UVRT power control mode (MpUVRT).  It is a project-dependent parameter. true = voltage control (1 in
      the IEC model) false = reactive power control (0 in the IEC model).
    omegaoffset: Offset to reference value that limits controller action during rotor speed changes (omegaoffset). It is
      a case-dependent parameter.
    pdtdmax: Maximum active drive train damping power (pDTDmax). It is a type-dependent parameter.
    tdvs: Time delay after deep voltage sags (TDVS) (>= 0). It is a project-dependent parameter.
    thetaemin: Minimum electrical generator torque (temin). It is a type-dependent parameter.
    thetauscale: Voltage scaling factor of reset-torque (tuscale). It is a project-dependent parameter.
    tomegafiltp3: Filter time constant for generator speed measurement (Tomegafiltp3) (>= 0). It is a type-dependent
      parameter.
    tpfiltp3: Filter time constant for power measurement (Tpfiltp3) (>= 0). It is a type-dependent parameter.
    tpord: Time constant in power order lag (Tpord). It is a type-dependent parameter.
    tufiltp3: Filter time constant for voltage measurement (Tufiltp3) (>= 0). It is a type-dependent parameter.
    tomegaref: Time constant in speed reference filter (Tomega,ref) (>= 0). It is a type-dependent parameter.
    udvs: Voltage limit for hold UVRT status after deep voltage sags (uDVS). It is a project-dependent parameter.
    updip: Voltage dip threshold for P-control (uPdip).  Part of turbine control, often different (e.g 0.8) from
      converter thresholds. It is a project-dependent parameter.
    omegadtd: Active drive train damping frequency (omegaDTD). It can be calculated from two mass model parameters. It
      is a type-dependent parameter.
    zeta: Coefficient for active drive train damping (zeta). It is a type-dependent parameter.
    WindTurbineType3IEC: Wind turbine type 3 model with which this wind control P type 3 model is associated.
    WindDynamicsLookupTable: The wind dynamics lookup table associated with this P control type 3 model.
    """

    dpmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dprefmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dprefmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dthetamax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dthetamaxuvrt: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kdtd: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kip: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kpp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    mpuvrt: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    omegaoffset: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pdtdmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tdvs: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    thetaemin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    thetauscale: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tomegafiltp3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tpfiltp3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tpord: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tufiltp3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tomegaref: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    udvs: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    updip: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    omegadtd: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    zeta: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType3IEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # WindDynamicsLookupTable : list = Field(default_factory=list, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
