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
class ExcANS(ExcitationSystemDynamics, ModuleType):
    """
    Italian excitation system. It represents static field voltage or excitation current feedback excitation system.

    k3: AVR gain (K3).  Typical value = 1000.
    k2: Exciter gain (K2).  Typical value = 20.
    kce: Ceiling factor (KCE).  Typical value = 1.
    t3: Time constant (T3) (>= 0).  Typical value = 1,6.
    t2: Time constant (T2) (>= 0).  Typical value = 0,05.
    t1: Time constant (T1) (>= 0).  Typical value = 20.
    blint: Governor control flag (BLINT).  0 = lead-lag regulator 1 = proportional integral regulator. Typical value =
      0.
    kvfif: Rate feedback signal flag (KVFIF).  0 = output voltage of the exciter 1 = exciter field current. Typical
      value = 0.
    ifmn: Minimum exciter current (IFMN).  Typical value = -5,2.
    ifmx: Maximum exciter current (IFMX).  Typical value = 6,5.
    vrmn: Minimum AVR output (VRMN).  Typical value = -5,2.
    vrmx: Maximum AVR output (VRMX).  Typical value = 6,5.
    krvecc: Feedback enabling (KRVECC).  0 = open loop control 1 = closed loop control. Typical value = 1.
    tb: Exciter time constant (TB) (>= 0).  Typical value = 0,04.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ExcANS(*args, **kwargs)

    k3: float = Field(
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

    kce: float = Field(
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

    t2: int = Field(
        default=0,
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

    blint: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kvfif: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ifmn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ifmx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vrmn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vrmx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    krvecc: int = Field(
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
# "import ExcANS"
# work as well as
# "from ExcANS import ExcANS".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ExcANS
