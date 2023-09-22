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
class ExcAVR7(ExcitationSystemDynamics, ModuleType):
    """
    IVO excitation system.

    k1: Gain (K1).  Typical value = 1.
    a1: Lead coefficient (A1).  Typical value = 0,5.
    a2: Lag coefficient (A2).  Typical value = 0,5.
    t1: Lead time constant (T1) (>= 0).  Typical value = 0,05.
    t2: Lag time constant (T2) (>= 0).  Typical value = 0,1.
    vmax1: Lead-lag maximum limit (Vmax1) (> ExcAVR7.vmin1).  Typical value = 5.
    vmin1: Lead-lag minimum limit (Vmin1) (< ExcAVR7.vmax1).  Typical value = -5.
    k3: Gain (K3).  Typical value = 3.
    a3: Lead coefficient (A3).  Typical value = 0,5.
    a4: Lag coefficient (A4).  Typical value = 0,5.
    t3: Lead time constant (T3) (>= 0).  Typical value = 0,1.
    t4: Lag time constant (T4) (>= 0).  Typical value = 0,1.
    vmax3: Lead-lag maximum limit (Vmax3) (> ExcAVR7.vmin3).  Typical value = 5.
    vmin3: Lead-lag minimum limit (Vmin3) (< ExcAVR7.vmax3).  Typical value = -5.
    k5: Gain (K5).  Typical value = 1.
    a5: Lead coefficient (A5).  Typical value = 0,5.
    a6: Lag coefficient (A6).  Typical value = 0,5.
    t5: Lead time constant (T5) (>= 0).  Typical value = 0,1.
    t6: Lag time constant (T6) (>= 0).  Typical value = 0,1.
    vmax5: Lead-lag maximum limit (Vmax5) (> ExcAVR7.vmin5).  Typical value = 5.
    vmin5: Lead-lag minimum limit (Vmin5) (< ExcAVR7.vmax5).  Typical value = -2.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ExcAVR7(*args, **kwargs)

    k1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

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

    vmax1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vmin1: float = Field(
        default=0.0,
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

    a3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a4: float = Field(
        default=0.0,
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

    vmax3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vmin3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k5: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a5: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a6: float = Field(
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

    vmax5: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vmin5: float = Field(
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
# "import ExcAVR7"
# work as well as
# "from ExcAVR7 import ExcAVR7".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ExcAVR7
