"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcAC2A(ExcitationSystemDynamics, ModuleType):
    """
    Modified IEEE AC2A alternator-supplied rectifier excitation system with different field current limit.

    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.
    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 400.
    ta: Voltage regulator time constant (Ta) (> 0).  Typical value = 0,02.
    vamax: Maximum voltage regulator output (Vamax) (> 0).  Typical value = 8.
    vamin: Minimum voltage regulator output (Vamin) (< 0).  Typical value = -8.
    kb: Second stage regulator gain (Kb) (> 0).  Exciter field current controller gain.  Typical value = 25.
    kb1: Second stage regulator gain (Kb1). It is exciter field current controller gain used as alternative to Kb to
      represent a variant of the ExcAC2A model.  Typical value = 25.
    vrmax: Maximum voltage regulator outputs (Vrmax) (> 0).  Typical value = 105.
    vrmin: Minimum voltage regulator outputs (Vrmin) (< 0).  Typical value = -95.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,6.
    vfemax: Exciter field current limit reference (Vfemax) (>= 0).  Typical value = 4,4.
    kh: Exciter field current feedback gain (Kh) (>= 0).  Typical value = 1.
    kf: Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0,03.
    kl: Exciter field current limiter gain (Kl).  Typical value = 10.
    vlr: Maximum exciter field current (Vlr) (> 0).  Typical value = 4,4.
    kl1: Coefficient to allow different usage of the model (Kl1).  Typical value = 1.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks) (>= 0).  Typical value = 0.
    tf: Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 1.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 0,28.
    kd: Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 0,35.
    ke: Exciter constant related to self-excited field (Ke).  Typical value = 1.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) (> 0).
      Typical value = 4,4.
    seve1: Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance
      (Se[Ve1]) (>= 0).  Typical value = 0,037.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2) (> 0).
      Typical value = 3,3.
    seve2: Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance
      (Se[Ve2]) (>= 0).  Typical value = 0,012.
    hvgate: Indicates if HV gate is active (HVgate). true = gate is used false = gate is not used. Typical value = true.
    lvgate: Indicates if LV gate is active (LVgate). true = gate is used false = gate is not used. Typical value = true.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ExcAC2A(*args, **kwargs)

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

    kb: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kb1: float = Field(
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

    vfemax: float = Field(
        default=0.0,
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

    kf: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kl: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vlr: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kl1: float = Field(
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

    tf: int = Field(
        default=0,
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

    hvgate: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    lvgate: bool = Field(
        default=False,
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


# This + inheriting from ModuleType + __call__:
# makes:
# "import ExcAC2A"
# work as well as
# "from ExcAC2A import ExcAC2A".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ExcAC2A
