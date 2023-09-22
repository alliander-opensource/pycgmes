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

from .SynchronousMachineDetailed import SynchronousMachineDetailed


@dataclass(config=DataclassConfig)
class SynchronousMachineTimeConstantReactance(SynchronousMachineDetailed, ModuleType):
    """
    Synchronous machine detailed modelling types are defined by the combination of the attributes
      SynchronousMachineTimeConstantReactance.modelType and SynchronousMachineTimeConstantReactance.rotorType.
      Parameter details:  The "p" in the time-related attribute names is a substitution for a "prime" in the usual
      parameter notation, e.g. tpdo refers to T'do. The parameters used for models expressed in time constant
      reactance form include:  - RotatingMachine.ratedS (MVAbase); - RotatingMachineDynamics.damping (D); -
      RotatingMachineDynamics.inertia (H); - RotatingMachineDynamics.saturationFactor (S1); -
      RotatingMachineDynamics.saturationFactor120 (S12); - RotatingMachineDynamics.statorLeakageReactance (Xl); -
      RotatingMachineDynamics.statorResistance (Rs); - SynchronousMachineTimeConstantReactance.ks (Ks); -
      SynchronousMachineDetailed.saturationFactorQAxis (S1q); - SynchronousMachineDetailed.saturationFactor120QAxis
      (S12q); - SynchronousMachineDetailed.efdBaseRatio; - SynchronousMachineDetailed.ifdBaseType; - .xDirectSync
      (Xd); - .xDirectTrans (X'd); - .xDirectSubtrans (X''d); - .xQuadSync (Xq); - .xQuadTrans (X'q); -
      .xQuadSubtrans (X''q); - .tpdo (T'do); - .tppdo (T''do); - .tpqo (T'qo); - .tppqo (T''qo); - .tc.

    rotorType: Type of rotor on physical machine.
    modelType: Type of synchronous machine model used in dynamic simulation applications.
    ks: Saturation loading correction factor (Ks) (>= 0).  Used only by type J model.  Typical value = 0.
    xDirectSync: Direct-axis synchronous reactance (Xd) (>= SynchronousMachineTimeConstantReactance.xDirectTrans). The
      quotient of a sustained value of that AC component of armature voltage that is produced by the
      total direct-axis flux due to direct-axis armature current and the value of the AC component of
      this current, the machine running at rated speed.  Typical value = 1,8.
    xDirectTrans: Direct-axis transient reactance (unsaturated) (X`d) (>=
      SynchronousMachineTimeConstantReactance.xDirectSubtrans).  Typical value = 0,5.
    xDirectSubtrans: Direct-axis subtransient reactance (unsaturated) (X``d) (>
      RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.
    xQuadSync: Quadrature-axis synchronous reactance (Xq) (>= SynchronousMachineTimeConstantReactance.xQuadTrans). The
      ratio of the component of reactive armature voltage, due to the quadrature-axis component of
      armature current, to this component of current, under steady state conditions and at rated
      frequency.  Typical value = 1,6.
    xQuadTrans: Quadrature-axis transient reactance (X`q) (>= SynchronousMachineTimeConstantReactance.xQuadSubtrans).
      Typical value = 0,3.
    xQuadSubtrans: Quadrature-axis subtransient reactance (X``q) (> RotatingMachineDynamics.statorLeakageReactance).
      Typical value = 0,2.
    tpdo: Direct-axis transient rotor time constant (T`do) (> SynchronousMachineTimeConstantReactance.tppdo).  Typical
      value = 5.
    tppdo: Direct-axis subtransient rotor time constant (T``do) (> 0).  Typical value = 0,03.
    tpqo: Quadrature-axis transient rotor time constant (T`qo) (> SynchronousMachineTimeConstantReactance.tppqo).
      Typical value = 0,5.
    tppqo: Quadrature-axis subtransient rotor time constant (T``qo) (> 0). Typical value = 0,03.
    tc: Damping time constant for `Canay` reactance (>= 0).  Typical value = 0.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return SynchronousMachineTimeConstantReactance(*args, **kwargs)

    rotorType: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    modelType: Optional[str] = Field(
        default=None,
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

    xDirectSync: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    xDirectTrans: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    xDirectSubtrans: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    xQuadSync: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    xQuadTrans: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    xQuadSubtrans: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tpdo: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tppdo: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tpqo: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tppqo: int = Field(
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
# "import SynchronousMachineTimeConstantReactance"
# work as well as
# "from SynchronousMachineTimeConstantReactance import SynchronousMachineTimeConstantReactance".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = SynchronousMachineTimeConstantReactance
