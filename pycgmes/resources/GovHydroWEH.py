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
class GovHydroWEH(TurbineGovernorDynamics):
    """
    WoodwardTM electric hydro governor.  [Footnote: Woodward electric hydro governors are an example of suitable
      products available commercially. This information is given for the convenience of users of this document and
      does not constitute an endorsement by IEC of these products.]

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    rpg: Permanent droop for governor output feedback (R-Perm-Gate).
    rpp: Permanent droop for electrical power feedback (R-Perm-Pe).
    tpe: Electrical power droop time constant (Tpe) (>= 0).
    kp: Derivative control gain (Kp).
    ki: Derivative controller Integral gain (Ki).
    kd: Derivative controller derivative gain (Kd).
    td: Derivative controller time constant (Td) (>= 0).  Limits the derivative characteristic beyond a breakdown
      frequency to avoid amplification of high-frequency noise.
    tp: Pilot valve time lag time constant (Tp) (>= 0).
    tdv: Distributive valve time lag time constant (Tdv) (>= 0).
    tg: Value to allow the distribution valve controller to advance beyond the gate movement rate limit (Tg) (>= 0).
    gtmxop: Maximum gate opening rate (Gtmxop).
    gtmxcl: Maximum gate closing rate (Gtmxcl).
    gmax: Maximum gate position (Gmax) (> GovHydroWEH.gmin).
    gmin: Minimum gate position (Gmin) (< GovHydroWEH.gmax).
    dturb: Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU).
    tw: Water inertia time constant (Tw) (> 0).
    db: Speed deadband (db).
    dpv: Value to allow the pilot valve controller to advance beyond the gate limits (Dpv).
    dicn: Value to allow the integral controller to advance beyond the gate limits (Dicn).
    feedbackSignal: Feedback signal selection (Sw). true = PID output (if R-Perm-Gate = droop and R-Perm-Pe = 0) false =
      electrical power (if R-Perm-Gate = 0 and R-Perm-Pe = droop) or false = gate position (if
      R-Perm-Gate = droop and R-Perm-Pe = 0). Typical value = false.
    gv1: Gate 1 (Gv1).  Gate Position value for point 1 for lookup table representing water flow through the turbine as
      a function of gate position to produce steady state flow.
    gv2: Gate 2 (Gv2).  Gate Position value for point 2 for lookup table representing water flow through the turbine as
      a function of gate position to produce steady state flow.
    gv3: Gate 3 (Gv3).  Gate Position value for point 3 for lookup table representing water flow through the turbine as
      a function of gate position to produce steady state flow.
    gv4: Gate 4 (Gv4).  Gate Position value for point 4 for lookup table representing water flow through the turbine as
      a function of gate position to produce steady state flow.
    gv5: Gate 5 (Gv5).  Gate Position value for point 5 for lookup table representing water flow through the turbine as
      a function of gate position to produce steady state flow.
    fl1: Flowgate 1 (Fl1).  Flow value for gate position point 1 for lookup table representing water flow through the
      turbine as a function of gate position to produce steady state flow.
    fl2: Flowgate 2 (Fl2).  Flow value for gate position point 2 for lookup table representing water flow through the
      turbine as a function of gate position to produce steady state flow.
    fl3: Flowgate 3 (Fl3).  Flow value for gate position point 3 for lookup table representing water flow through the
      turbine as a function of gate position to produce steady state flow.
    fl4: Flowgate 4 (Fl4).  Flow value for gate position point 4 for lookup table representing water flow through the
      turbine as a function of gate position to produce steady state flow.
    fl5: Flowgate 5 (Fl5).  Flow value for gate position point 5 for lookup table representing water flow through the
      turbine as a function of gate position to produce steady state flow.
    fp1: Flow P1 (Fp1).  Turbine flow value for point 1 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp2: Flow P2 (Fp2).  Turbine flow value for point 2 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp3: Flow P3 (Fp3).  Turbine flow value for point 3 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp4: Flow P4 (Fp4).  Turbine flow value for point 4 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp5: Flow P5 (Fp5).  Turbine flow value for point 5 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp6: Flow P6 (Fp6).  Turbine flow value for point 6 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp7: Flow P7 (Fp7).  Turbine flow value for point 7 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp8: Flow P8 (Fp8).  Turbine flow value for point 8 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp9: Flow P9 (Fp9).  Turbine flow value for point 9 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp10: Flow P10 (Fp10).  Turbine flow value for point 10 for lookup table representing PU mechanical power on machine
      MVA rating as a function of turbine flow.
    pmss1: Pmss flow P1 (Pmss1).  Mechanical power output for turbine flow point 1 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss2: Pmss flow P2 (Pmss2).  Mechanical power output for turbine flow point 2 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss3: Pmss flow P3 (Pmss3).  Mechanical power output for turbine flow point 3 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss4: Pmss flow P4 (Pmss4).  Mechanical power output for turbine flow point 4 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss5: Pmss flow P5 (Pmss5).  Mechanical power output for turbine flow point 5 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss6: Pmss flow P6 (Pmss6).  Mechanical power output for turbine flow point 6 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss7: Pmss flow P7 (Pmss7).  Mechanical power output for turbine flow point 7 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss8: Pmss flow P8 (Pmss8).  Mechanical power output for turbine flow point 8 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss9: Pmss flow P9 (Pmss9).  Mechanical power output for turbine flow point 9 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss10: Pmss flow P10 (Pmss10).  Mechanical power output for turbine flow point 10 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    """

    mwbase: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rpg: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rpp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tpe: int = Field(
        default=0,
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

    td: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tp: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tdv: int = Field(
        default=0,
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

    gtmxop: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gtmxcl: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dturb: float = Field(
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

    db: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dpv: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dicn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    feedbackSignal: bool = Field(
        default=False,
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

    gv2: float = Field(
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

    gv4: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gv5: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fl1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fl2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fl3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fl4: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fl5: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fp1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fp2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fp3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fp4: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fp5: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fp6: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fp7: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fp8: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fp9: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fp10: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmss1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmss2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmss3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmss4: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmss5: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmss6: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmss7: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmss8: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmss9: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmss10: float = Field(
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
