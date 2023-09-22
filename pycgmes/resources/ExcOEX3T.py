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
class ExcOEX3T(ExcitationSystemDynamics, ModuleType):
    """
    Modified IEEE type ST1 excitation system with semi-continuous and acting terminal voltage limiter.

    t1: Time constant (T1) (>= 0).
    t2: Time constant (T2) (>= 0).
    t3: Time constant (T3) (>= 0).
    t4: Time constant (T4) (>= 0).
    ka: Gain (KA).
    t5: Time constant (T5) (>= 0).
    t6: Time constant (T6) (>= 0).
    vrmax: Limiter (VRMAX) (> ExcOEX3T.vrmin).
    vrmin: Limiter (VRMIN) (< ExcOEX3T.vrmax).
    te: Time constant (TE) (>= 0).
    kf: Gain (KF).
    tf: Time constant (TF) (>= 0).
    kc: Gain (KC).
    kd: Gain (KD).
    ke: Gain (KE).
    e1: Saturation parameter (E1).
    see1: Saturation parameter (SE[E1]).
    e2: Saturation parameter (E2).
    see2: Saturation parameter (SE[E2]).
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ExcOEX3T(*args, **kwargs)

    t1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t4: int = Field(
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

    t5: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t6: int = Field(
        default=0,
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

    e1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    see1: float = Field(
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

    see2: float = Field(
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
# "import ExcOEX3T"
# work as well as
# "from ExcOEX3T import ExcOEX3T".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ExcOEX3T
