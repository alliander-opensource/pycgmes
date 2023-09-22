"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcREXS(ExcitationSystemDynamics, ModuleType):
    """
    General purpose rotating excitation system.  This model can be used to represent a wide range of excitation systems
      whose DC power source is an AC or DC generator. It encompasses IEEE type AC1, AC2, DC1, and DC2 excitation
      system models.

    e1: Field voltage value 1 (E1).  Typical value = 3.
    e2: Field voltage value 2 (E2).  Typical value = 4.
    fbf: Rate feedback signal flag (fbf). Typical value = fieldCurrent.
    flimf: Limit type flag (Flimf).  Typical value = 0.
    kc: Rectifier regulation factor (Kc).  Typical value = 0,05.
    kd: Exciter regulation factor (Kd).  Typical value = 2.
    ke: Exciter field proportional constant (Ke).  Typical value = 1.
    kefd: Field voltage feedback gain (Kefd).  Typical value = 0.
    kf: Rate feedback gain (Kf) (>= 0).  Typical value = 0,05.
    kh: Field voltage controller feedback gain (Kh).  Typical value = 0.
    kii: Field current regulator integral gain (Kii).  Typical value = 0.
    kip: Field current regulator proportional gain (Kip).  Typical value = 1.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical value = 0.
    kvi: Voltage regulator integral gain (Kvi).  Typical value = 0.
    kvp: Voltage regulator proportional gain (Kvp).  Typical value = 2800.
    kvphz: V/Hz limiter gain (Kvphz).  Typical value = 0.
    nvphz: Pickup speed of V/Hz limiter (Nvphz).  Typical value = 0.
    se1: Saturation factor at E1 (Se1).  Typical value = 0,0001.
    se2: Saturation factor at E2 (Se2).  Typical value = 0,001.
    ta: Voltage regulator time constant (Ta) (>= 0).  If = 0, block is bypassed.  Typical value = 0,01.
    tb1: Lag time constant (Tb1) (>= 0).  If = 0, block is bypassed.  Typical value = 0.
    tb2: Lag time constant (Tb2) (>= 0).  If = 0, block is bypassed.  Typical value = 0.
    tc1: Lead time constant (Tc1) (>= 0).  Typical value = 0.
    tc2: Lead time constant (Tc2) (>= 0).  Typical value = 0.
    te: Exciter field time constant (Te) (> 0).  Typical value = 1,2.
    tf: Rate feedback time constant (Tf) (>= 0).  If = 0, the feedback path is not used.  Typical value = 1.
    tf1: Feedback lead time constant (Tf1) (>= 0).  Typical value = 0.
    tf2: Feedback lag time constant (Tf2) (>= 0).  If = 0, block is bypassed.  Typical value = 0.
    tp: Field current bridge time constant (Tp) (>= 0).  Typical value = 0.
    vcmax: Maximum compounding voltage (Vcmax).  Typical value = 0.
    vfmax: Maximum exciter field current (Vfmax) (> ExcREXS.vfmin).  Typical value = 47.
    vfmin: Minimum exciter field current (Vfmin) (< ExcREXS.vfmax).  Typical value = -20.
    vimax: Voltage regulator input limit (Vimax).  Typical value = 0,1.
    vrmax: Maximum controller output (Vrmax) (> ExcREXS.vrmin).  Typical value = 47.
    vrmin: Minimum controller output (Vrmin) (< ExcREXS.vrmax).  Typical value = -20.
    xc: Exciter compounding reactance (Xc).  Typical value = 0.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ExcREXS(*args, **kwargs)

    e1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    e2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    fbf: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    flimf: float = Field(
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

    kefd: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kf: int = Field(
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

    kii: float = Field(
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

    ks: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kvi: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kvp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kvphz: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    nvphz: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    se1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    se2: float = Field(
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

    tb1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tb2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tc1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tc2: int = Field(
        default=0,
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

    tf: int = Field(
        default=0,
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

    tp: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vcmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vfmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vfmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vimax: float = Field(
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

    xc: float = Field(
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
# "import ExcREXS"
# work as well as
# "from ExcREXS import ExcREXS".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ExcREXS
