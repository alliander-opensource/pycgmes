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
class ExcAC3A(ExcitationSystemDynamics):
    """
    Modified IEEE AC3A alternator-supplied rectifier excitation system with different field current limit.

    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.
    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 45,62.
    ta: Voltage regulator time constant (Ta) (> 0).  Typical value = 0,013.
    vamax: Maximum voltage regulator output (Vamax) (> 0).  Typical value = 1.
    vamin: Minimum voltage regulator output (Vamin) (< 0).  Typical value = -0,95.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1,17.
    vemin: Minimum exciter voltage output (Vemin) (<= 0).  Typical value = 0.
    kr: Constant associated with regulator and alternator field power supply (Kr) (> 0).  Typical value =3,77.
    kf: Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0,143.
    tf: Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 1.
    kn: Excitation control system stabilizer gain (Kn) (>= 0).  Typical value =0,05.
    efdn: Value of Efd at which feedback gain changes (Efdn) (> 0).  Typical value = 2,36.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 0,104.
    kd: Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 0,499.
    ke: Exciter constant related to self-excited field (Ke).  Typical value = 1.
    klv: Gain used in the minimum field voltage limiter loop (Klv).  Typical value = 0,194.
    kf1: Coefficient to allow different usage of the model (Kf1).  Typical value = 1.
    kf2: Coefficient to allow different usage of the model (Kf2).  Typical value = 0.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical value = 0.
    vfemax: Exciter field current limit reference (Vfemax) (>= 0).  Typical value = 16.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) (> 0).
      Typical value = 6.24.
    seve1: Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance
      (Se[Ve1]) (>= 0).  Typical value = 1,143.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2) (> 0).
      Typical value = 4,68.
    seve2: Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance
      (Se[Ve2]) (>= 0).  Typical value = 0,1.
    vlv: Field voltage used in the minimum field voltage limiter loop (Vlv).  Typical value = 0,79.
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

    ka: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ta: float = Field(
        default=0.0,
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

    klv: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kf1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kf2: float = Field(
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

    vlv: float = Field(
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
