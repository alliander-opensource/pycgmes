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

from .SynchronousMachineDetailed import SynchronousMachineDetailed


@dataclass(config=DataclassConfig)
class SynchronousMachineEquivalentCircuit(SynchronousMachineDetailed, ModuleType):
    """
    The electrical equations for all variations of the synchronous models are based on the SynchronousEquivalentCircuit
      diagram for the direct- and quadrature- axes. Equations for conversion between equivalent circuit and time
      constant reactance forms: Xd = Xad + Xl X'd = Xl + Xad x Xfd / (Xad + Xfd) X"d = Xl + Xad x Xfd x X1d / (Xad x
      Xfd + Xad x X1d + Xfd x X1d) Xq = Xaq + Xl X'q = Xl + Xaq x X1q / (Xaq + X1q) X"q = Xl + Xaq x X1q x X2q /
      (Xaq x X1q + Xaq x X2q + X1q x X2q) T'do = (Xad + Xfd) / (omega0 x Rfd) T"do = (Xad x Xfd + Xad x X1d + Xfd x
      X1d) / (omega0 x R1d x (Xad + Xfd) T'qo = (Xaq + X1q) / (omega0 x R1q) T"qo = (Xaq x X1q + Xaq x X2q + X1q x
      X2q) / (omega0 x R2q x (Xaq + X1q) Same equations using CIM attributes from
      SynchronousMachineTimeConstantReactance class on left of "=" and SynchronousMachineEquivalentCircuit class on
      right (except as noted): xDirectSync = xad + RotatingMachineDynamics.statorLeakageReactance xDirectTrans =
      RotatingMachineDynamics.statorLeakageReactance + xad x xfd / (xad + xfd) xDirectSubtrans =
      RotatingMachineDynamics.statorLeakageReactance + xad x xfd x x1d / (xad x xfd + xad x x1d + xfd x x1d)
      xQuadSync = xaq + RotatingMachineDynamics.statorLeakageReactance xQuadTrans =
      RotatingMachineDynamics.statorLeakageReactance + xaq x x1q / (xaq+ x1q) xQuadSubtrans =
      RotatingMachineDynamics.statorLeakageReactance + xaq x x1q x x2q / (xaq x x1q + xaq x x2q + x1q x x2q)  tpdo =
      (xad + xfd) / (2 x pi x nominal frequency x rfd) tppdo = (xad x xfd + xad x x1d + xfd x x1d) / (2 x pi x
      nominal frequency x r1d x (xad + xfd) tpqo = (xaq + x1q) / (2 x pi x nominal frequency x r1q) tppqo = (xaq x
      x1q + xaq x x2q + x1q x x2q) / (2 x pi x nominal frequency x r2q x (xaq + x1q) These are only valid for a
      simplified model where "Canay" reactance is zero.

    xad: Direct-axis mutual reactance.
    rfd: Field winding resistance.
    xfd: Field winding leakage reactance.
    r1d: Direct-axis damper 1 winding resistance.
    x1d: Direct-axis damper 1 winding leakage reactance.
    xf1d: Differential mutual (`Canay`) reactance.
    xaq: Quadrature-axis mutual reactance.
    r1q: Quadrature-axis damper 1 winding resistance.
    x1q: Quadrature-axis damper 1 winding leakage reactance.
    r2q: Quadrature-axis damper 2 winding resistance.
    x2q: Quadrature-axis damper 2 winding leakage reactance.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return SynchronousMachineEquivalentCircuit(*args, **kwargs)

    xad: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rfd: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    xfd: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    r1d: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    x1d: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    xf1d: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    xaq: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    r1q: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    x1q: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    r2q: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    x2q: float = Field(
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
# "import SynchronousMachineEquivalentCircuit"
# work as well as
# "from SynchronousMachineEquivalentCircuit import SynchronousMachineEquivalentCircuit".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = SynchronousMachineEquivalentCircuit
