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
class ExcIEEEAC2A(ExcitationSystemDynamics, ModuleType):
    """
    IEEE 421.5-2005 type AC2A model. The model represents a high initial response field-controlled alternator-rectifier
      excitation system. The alternator main exciter is used with non-controlled rectifiers. The type AC2A model is
      similar to that of type AC1A except for the inclusion of exciter time constant compensation and exciter field
      current limiting elements. Reference: IEEE 421.5-2005, 6.2.

    tb: Voltage regulator time constant (TB) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (TC) (>= 0).  Typical value = 0.
    ka: Voltage regulator gain (KA) (> 0).  Typical value = 400.
    ta: Voltage regulator time constant (TA) (> 0).  Typical value = 0,02.
    vamax: Maximum voltage regulator output (VAMAX) (> 0).  Typical value = 8.
    vamin: Minimum voltage regulator output (VAMIN) (< 0).  Typical value = -8.
    kb: Second stage regulator gain (KB) (> 0).  Typical value = 25.
    vrmax: Maximum voltage regulator outputs (VRMAX) (> 0).  Typical value = 105.
    vrmin: Minimum voltage regulator outputs (VRMIN) (< 0).  Typical value = -95.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 0,6.
    vfemax: Exciter field current limit reference (VFEMAX) (> 0).  Typical value = 4,4.
    kh: Exciter field current feedback gain (KH) (>= 0).  Typical value = 1.
    kf: Excitation control system stabilizer gains (KF) (>= 0).  Typical value = 0,03.
    tf: Excitation control system stabilizer time constant (TF) (> 0).  Typical value = 1.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0).  Typical value = 0,28.
    kd: Demagnetizing factor, a function of exciter alternator reactances (KD) (>= 0).  Typical value = 0,35.
    ke: Exciter constant related to self-excited field (KE) (>= 0).  Typical value = 1.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE1) (> 0).
      Typical value = 4,4.
    seve1: Exciter saturation function value at the corresponding exciter voltage, VE1, back of commutating reactance
      (SE[VE1]) (>= 0).  Typical value = 0,037.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE2) (> 0).
      Typical value = 3,3.
    seve2: Exciter saturation function value at the corresponding exciter voltage, VE2, back of commutating reactance
      (SE[VE2]) (>= 0).  Typical value = 0,012.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ExcIEEEAC2A(*args, **kwargs)

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
# "import ExcIEEEAC2A"
# work as well as
# "from ExcIEEEAC2A import ExcIEEEAC2A".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ExcIEEEAC2A
