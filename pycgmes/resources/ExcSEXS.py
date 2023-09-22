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
class ExcSEXS(ExcitationSystemDynamics, ModuleType):
    """
    Simplified excitation system.

    tatb: Gain reduction ratio of lag-lead element ([Ta / Tb]).  Typical value = 0,1.
    tb: Denominator time constant of lag-lead block (Tb) (>= 0).  Typical value = 10.
    k: Gain (K) (> 0).  Typical value = 100.
    te: Time constant of gain block (Te) (> 0).  Typical value = 0,05.
    emin: Minimum field voltage output (Emin) (< ExcSEXS.emax).  Typical value = -5.
    emax: Maximum field voltage output (Emax) (> ExcSEXS.emin).  Typical value = 5.
    kc: PI controller gain (Kc) (> 0 if ExcSEXS.tc > 0).  Typical value = 0,08.
    tc: PI controller phase lead time constant (Tc) (>= 0).  Typical value = 0.
    efdmin: Field voltage clipping minimum limit (Efdmin) (< ExcSEXS.efdmax).  Typical value = -5.
    efdmax: Field voltage clipping maximum limit (Efdmax) (> ExcSEXS.efdmin).  Typical value = 5.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ExcSEXS(*args, **kwargs)

    tatb: float = Field(
        default=0.0,
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

    k: float = Field(
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

    emin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    emax: float = Field(
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

    tc: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efdmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efdmax: float = Field(
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
# "import ExcSEXS"
# work as well as
# "from ExcSEXS import ExcSEXS".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ExcSEXS
