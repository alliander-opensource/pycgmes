"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcIEEEAC6A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type AC6A model. The model represents field-controlled alternator-rectifier excitation systems with
      system-supplied electronic voltage regulators.  The maximum output of the regulator, VR, is a function of
      terminal voltage, VT. The field current limiter included in the original model AC6A remains in the 2005
      update. Reference: IEEE 421.5-2005, 6.6.

    ka: Voltage regulator gain (KA) (> 0).  Typical value = 536.
    ta: Voltage regulator time constant (TA) (>= 0).  Typical value = 0,086.
    tk: Voltage regulator time constant (TK) (>= 0).  Typical value = 0,18.
    tb: Voltage regulator time constant (TB) (>= 0).  Typical value = 9.
    tc: Voltage regulator time constant (TC) (>= 0).  Typical value = 3.
    vamax: Maximum voltage regulator output (VAMAX) (> 0).  Typical value = 75.
    vamin: Minimum voltage regulator output (VAMIN) (< 0).  Typical value = -75.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 44.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0).  Typical value = -36.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 1.
    kh: Exciter field current limiter gain (KH) (>= 0).  Typical value = 92.
    tj: Exciter field current limiter time constant (TJ) (>= 0).  Typical value = 0,02.
    th: Exciter field current limiter time constant (TH) (> 0).  Typical value = 0,08.
    vfelim: Exciter field current limit reference (VFELIM) (> 0).  Typical value = 19.
    vhmax: Maximum field current limiter signal reference (VHMAX) (> 0).  Typical value = 75.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0). Typical value = 0,173.
    kd: Demagnetizing factor, a function of exciter alternator reactances (KD) (>= 0).  Typical value = 1,91.
    ke: Exciter constant related to self-excited field (KE).  Typical value = 1,6.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE1) (> 0).
      Typical value = 7,4.
    seve1: Exciter saturation function value at the corresponding exciter voltage, VE1, back of commutating reactance
      (SE[VE1]) (>= 0).  Typical value = 0,214.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE2) (> 0).
      Typical value = 5,55.
    seve2: Exciter saturation function value at the corresponding exciter voltage, VE2, back of commutating reactance
      (SE[VE2]) (>= 0).  Typical value = 0,044.
    """

    ka: float = Field(
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
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
