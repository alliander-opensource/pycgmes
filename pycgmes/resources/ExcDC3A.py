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
class ExcDC3A(ExcitationSystemDynamics, ModuleType):
    """
    Modified IEEE DC3A direct current commutator exciter with speed input, and deadband.  DC old type 4.

    trh: Rheostat travel time (Trh) (> 0).  Typical value = 20.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical value = 0.
    kr: Deadband (Kr).  Typical value = 0.
    kv: Fast raise/lower contact setting (Kv) (> 0).  Typical value = 0,05.
    vrmax: Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 5.
    vrmin: Minimum voltage regulator output (Vrmin) (<= 0).  Typical value = 0.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1,83.
    ke: Exciter constant related to self-excited field (Ke).  Typical value = 1.
    efd1: Exciter voltage at which exciter saturation is defined (Efd1) (> 0).  Typical value = 2,6.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Efd1]) (>= 0).  Typical
      value = 0,1.
    efd2: Exciter voltage at which exciter saturation is defined (Efd2) (> 0).  Typical value = 3,45.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, Efd2 (Se[Efd2]) (>= 0).  Typical
      value = 0,35.
    exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is
      applied to integrator output false = a lower limit of zero not applied to integrator output. Typical
      value = true.
    efdmax: Maximum voltage exciter output limiter (Efdmax) (> ExcDC3A.efdmin).  Typical value = 99.
    efdmin: Minimum voltage exciter output limiter (Efdmin) (< ExcDC3A.efdmax).  Typical value = -99.
    efdlim: (Efdlim). true = exciter output limiter is active false = exciter output limiter not active. Typical value =
      true.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ExcDC3A(*args, **kwargs)

    trh: int = Field(
        default=0,
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

    kr: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kv: float = Field(
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

    ke: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efd1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    seefd1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efd2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    seefd2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    exclim: bool = Field(
        default=False,
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

    efdmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efdlim: bool = Field(
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
# "import ExcDC3A"
# work as well as
# "from ExcDC3A import ExcDC3A".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ExcDC3A
