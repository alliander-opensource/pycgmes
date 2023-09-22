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
class ExcAC4A(ExcitationSystemDynamics, ModuleType):
    """
    Modified IEEE AC4A alternator-supplied rectifier excitation system with different minimum controller output.

    vimax: Maximum voltage regulator input limit (Vimax)  (> 0).  Typical value = 10.
    vimin: Minimum voltage regulator input limit (Vimin) (< 0).  Typical value = -10.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 1.
    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 10.
    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 200.
    ta: Voltage regulator time constant (Ta) (> 0).  Typical value = 0,015.
    vrmax: Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 5,64.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -4,53.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 0.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ExcAC4A(*args, **kwargs)

    vimax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vimin: float = Field(
        default=0.0,
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

    tb: int = Field(
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

    kc: float = Field(
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
# "import ExcAC4A"
# work as well as
# "from ExcAC4A import ExcAC4A".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ExcAC4A
