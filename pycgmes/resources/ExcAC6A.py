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
class ExcAC6A(ExcitationSystemDynamics):
    """
    Modified IEEE AC6A alternator-supplied rectifier excitation system with speed input.

    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 536.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical value = 0.
    ta: Voltage regulator time constant (Ta) (>= 0).  Typical value = 0,086.
    tk: Voltage regulator time constant (Tk) (>= 0).  Typical value = 0,18.
    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 9.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 3.
    vamax: Maximum voltage regulator output (Vamax) (> 0).  Typical value = 75.
    vamin: Minimum voltage regulator output (Vamin) (< 0).  Typical value = -75.
    vrmax: Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 44.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -36.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1.
    kh: Exciter field current limiter gain (Kh) (>= 0).  Typical value = 92.
    tj: Exciter field current limiter time constant (Tj) (>= 0).  Typical value = 0,02.
    th: Exciter field current limiter time constant (Th) (> 0).  Typical value = 0,08.
    vfelim: Exciter field current limit reference (Vfelim) (> 0).  Typical value = 19.
    vhmax: Maximum field current limiter signal reference (Vhmax) (> 0).  Typical value = 75.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 0,173.
    kd: Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 1,91.
    ke: Exciter constant related to self-excited field (Ke).  Typical value = 1,6.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) (> 0).
      Typical value = 7,4.
    seve1: Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance
      (Se[Ve1]) (>= 0).  Typical value = 0,214.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2) (> 0).
      Typical value = 5,55.
    seve2: Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance
      (Se[Ve2]) (>= 0).  Typical value = 0,044.
    """

    ka: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ks: float = Field(
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

    tk: int = Field(
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

    tc: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vamax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vamin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vrmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vrmin: float = Field(
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

    kh: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tj: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    th: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vfelim: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vhmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kc: float = Field(
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

    ke: float = Field(
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

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
