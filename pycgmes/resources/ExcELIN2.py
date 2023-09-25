"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcELIN2(ExcitationSystemDynamics):
    """
    Detailed excitation system ELIN (VATECH).  This model represents an all-static excitation system. A PI voltage
      controller establishes a desired field current set point for a proportional current controller. The integrator
      of the PI controller has a follow-up input to match its signal to the present field current.  Power system
      stabilizer models used in conjunction with this excitation system model: PssELIN2, PssIEEE2B, Pss2B.

    k1: Voltage regulator input gain (K1).  Typical value = 0.
    k1ec: Voltage regulator input limit (K1ec).  Typical value = 2.
    kd1: Voltage controller derivative gain (Kd1).  Typical value = 34,5.
    tb1: Voltage controller derivative washout time constant (Tb1) (>= 0).  Typical value = 12,45.
    pid1max: Controller follow up gain (PID1max).  Typical value = 2.
    ti1: Controller follow up deadband (Ti1).  Typical value = 0.
    iefmax2: Minimum open circuit excitation voltage (Iefmax2).  Typical value = -5.
    k2: Gain (K2).  Typical value = 5.
    ketb: Gain (Ketb).  Typical value = 0,06.
    upmax: Limiter (Upmax) (> ExcELIN2.upmin).  Typical value = 3.
    upmin: Limiter (Upmin) (< ExcELIN2.upmax).  Typical value = 0.
    te: Time constant (Te) (>= 0).  Typical value = 0.
    xp: Excitation transformer effective reactance (Xp).  Typical value = 1.
    te2: Time Constant (Te2) (>= 0).  Typical value = 1.
    ke2: Gain (Ke2).  Typical value = 0,1.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) (> 0).
      Typical value = 3.
    seve1: Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance
      (Se[Ve1]) (>= 0).  Typical value = 0.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2) (> 0).
      Typical value = 0.
    seve2: Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance
      (Se[Ve2]) (>= 0).  Typical value = 1.
    tr4: Time constant (Tr4) (>= 0).  Typical value = 1.
    k3: Gain (K3).  Typical value = 0,1.
    ti3: Time constant (Ti3) (>= 0).  Typical value = 3.
    k4: Gain (K4).  Typical value = 0.
    ti4: Time constant (Ti4) (>= 0).  Typical value = 0.
    iefmax: Limiter (Iefmax) (> ExcELIN2.iefmin).  Typical value = 1.
    iefmin: Limiter (Iefmin) (< ExcELIN2.iefmax).  Typical value = 1.
    efdbas: Gain (Efdbas).  Typical value = 0,1.
    """

    k1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k1ec: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kd1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tb1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pid1max: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ti1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    iefmax2: float = Field(
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

    ketb: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    upmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    upmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    te: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    xp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    te2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ke2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ve1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    seve1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ve2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    seve2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tr4: int = Field(
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

    ti3: int = Field(
        default=0,
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

    ti4: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    iefmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    iefmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efdbas: float = Field(
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
