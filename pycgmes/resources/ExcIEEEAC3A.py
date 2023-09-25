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
class ExcIEEEAC3A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type AC3A model. The model represents the field-controlled alternator-rectifier excitation systems
      designated type AC3A. These excitation systems include an alternator main exciter with non-controlled
      rectifiers. The exciter employs self-excitation, and the voltage regulator power is derived from the exciter
      output voltage.  Therefore, this system has an additional nonlinearity, simulated by the use of a multiplier
      whose inputs are the voltage regulator command signal, Va, and the exciter output voltage, Efd, times KR.
      This model is applicable to excitation systems employing static voltage regulators. Reference: IEEE
      421.5-2005, 6.3.

    tb: Voltage regulator time constant (TB) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (TC) (>= 0).  Typical value = 0.
    ka: Voltage regulator gain (KA) (> 0).  Typical value = 45,62.
    ta: Voltage regulator time constant (TA) (> 0).  Typical value = 0,013.
    vamax: Maximum voltage regulator output (VAMAX) (> 0).  Typical value = 1.
    vamin: Minimum voltage regulator output (VAMIN) (< 0).  Typical value = -0,95.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 1,17.
    vemin: Minimum exciter voltage output (VEMIN) (<= 0).  Typical value = 0.
    kr: Constant associated with regulator and alternator field power supply (KR) (> 0).  Typical value = 3,77.
    kf: Excitation control system stabilizer gains (KF) (>= 0).  Typical value = 0,143.
    tf: Excitation control system stabilizer time constant (TF) (> 0).  Typical value = 1.
    kn: Excitation control system stabilizer gain (KN) (>= 0).  Typical value = 0,05.
    efdn: Value of Efd at which feedback gain changes (EFDN) (> 0).  Typical value = 2,36.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0).  Typical value = 0,104.
    kd: Demagnetizing factor, a function of exciter alternator reactances (KD) (>= 0).  Typical value = 0,499.
    ke: Exciter constant related to self-excited field (KE).  Typical value = 1.
    vfemax: Exciter field current limit reference (VFEMAX) (>= 0).  Typical value = 16.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE1) (> 0).
      Typical value = 6,24.
    seve1: Exciter saturation function value at the corresponding exciter voltage, VE1, back of commutating reactance
      (SE[VE1]) (>= 0).  Typical value = 1,143.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE2) (> 0).
      Typical value = 4,68.
    seve2: Exciter saturation function value at the corresponding exciter voltage, VE2, back of commutating reactance
      (SE[VE2]) (>= 0).  Typical value = 0,1.
    """

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

    te: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vemin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kr: float = Field(
        default=0.0,
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

    tf: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efdn: float = Field(
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

    vfemax: float = Field(
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
