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
class GovSteamFV4(TurbineGovernorDynamics):
    """
    Detailed electro-hydraulic governor for steam unit.

    kf1: Frequency bias (reciprocal of droop) (Kf1).  Typical value = 20.
    kf3: Frequency control (reciprocal of droop) (Kf3).  Typical value = 20.
    lps: Maximum positive power error (Lps).  Typical value = 0,03.
    lpi: Maximum negative power error (Lpi).  Typical value = -0,15.
    mxef: Upper limit for frequency correction (MXEF).  Typical value = 0,05.
    mnef: Lower limit for frequency correction (MNEF).  Typical value = -0,05.
    crmx: Maximum value of regulator set-point (Crmx).  Typical value = 1,2.
    crmn: Minimum value of regulator set-point (Crmn).  Typical value = 0.
    kpt: Proportional gain of electro-hydraulic regulator (Kpt).  Typical value = 0,3.
    kit: Integral gain of electro-hydraulic regulator (Kit).  Typical value = 0,04.
    rvgmx: Maximum value of integral regulator (Rvgmx).  Typical value = 1,2.
    rvgmn: Minimum value of integral regulator (Rvgmn).  Typical value = 0.
    svmx: Maximum regulator gate opening velocity (Svmx).  Typical value = 0,0333.
    svmn: Maximum regulator gate closing velocity (Svmn).  Typical value = -0,0333.
    srmx: Maximum valve opening (Srmx).  Typical value = 1,1.
    srmn: Minimum valve opening (Srmn).  Typical value = 0.
    kpp: Proportional gain of pressure feedback regulator (Kpp).  Typical value = 1.
    kip: Integral gain of pressure feedback regulator (Kip).  Typical value = 0,5.
    rsmimx: Maximum value of integral regulator (Rsmimx).  Typical value = 1,1.
    rsmimn: Minimum value of integral regulator (Rsmimn).  Typical value = 0.
    kmp1: First gain coefficient of  intercept valves characteristic (Kmp1).  Typical value = 0,5.
    kmp2: Second gain coefficient of intercept valves characteristic (Kmp2).  Typical value = 3,5.
    srsmp: Intercept valves characteristic discontinuity point (Srsmp).  Typical value = 0,43.
    ta: Control valves rate opening time (Ta) (>= 0).  Typical value = 0,8.
    tc: Control valves rate closing time (Tc) (>= 0).  Typical value = 0,5.
    ty: Control valves servo time constant (Ty) (>= 0).  Typical value = 0,1.
    yhpmx: Maximum control valve position (Yhpmx).  Typical value = 1,1.
    yhpmn: Minimum control valve position (Yhpmn).  Typical value = 0.
    tam: Intercept valves rate opening time (Tam) (>= 0).  Typical value = 0,8.
    tcm: Intercept valves rate closing time (Tcm) (>= 0).  Typical value = 0,5.
    ympmx: Maximum intercept valve position (Ympmx).  Typical value = 1,1.
    ympmn: Minimum intercept valve position (Ympmn).  Typical value = 0.
    y: Coefficient of linearized equations of turbine (Stodola formulation) (Y).  Typical value = 0,13.
    thp: High pressure (HP) time constant of the turbine (Thp) (>= 0).  Typical value = 0,15.
    trh: Reheater  time constant of the turbine (Trh) (>= 0).  Typical value = 10.
    tmp: Low pressure (LP) time constant of the turbine (Tmp) (>= 0).  Typical value = 0,4.
    khp: Fraction  of total turbine output generated by HP part (Khp).  Typical value = 0,35.
    pr1: First value of pressure set point static characteristic (Pr1).  Typical value = 0,2.
    pr2: Second value of pressure set point static characteristic, corresponding to Ps0 = 1,0 PU (Pr2).  Typical value =
      0,75.
    psmn: Minimum value of pressure set point static characteristic (Psmn).  Typical value = 1.
    kpc: Proportional gain of pressure regulator (Kpc).  Typical value = 0,5.
    kic: Integral gain of pressure regulator (Kic).  Typical value = 0,0033.
    kdc: Derivative gain of pressure regulator (Kdc).  Typical value = 1.
    tdc: Derivative time constant of pressure regulator (Tdc) (>= 0).  Typical value = 90.
    cpsmx: Maximum value of pressure regulator output (Cpsmx).  Typical value = 1.
    cpsmn: Minimum value of pressure regulator output (Cpsmn).  Typical value = -1.
    krc: Maximum variation of fuel flow (Krc).  Typical value = 0,05.
    tf1: Time constant of fuel regulation (Tf1) (>= 0).  Typical value = 10.
    tf2: Time constant of steam chest (Tf2) (>= 0).  Typical value = 10.
    tv: Boiler time constant (Tv) (>= 0).  Typical value = 60.
    ksh: Pressure loss due to flow friction in the boiler tubes (Ksh).  Typical value = 0,08.
    """

    kf1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kf3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    lps: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    lpi: float = Field(
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

    crmx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    crmn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kpt: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kit: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rvgmx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rvgmn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    svmx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    svmn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    srmx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    srmn: float = Field(
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

    kip: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rsmimx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rsmimn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kmp1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kmp2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    srsmp: float = Field(
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

    tc: int = Field(
        default=0,
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

    yhpmx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    yhpmn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tam: int = Field(
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

    ympmx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ympmn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    y: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    thp: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    trh: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tmp: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    khp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pr1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pr2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    psmn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kpc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kic: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kdc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tdc: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    cpsmx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    cpsmn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    krc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tf1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tf2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tv: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ksh: float = Field(
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
