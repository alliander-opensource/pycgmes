"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .SynchronousMachineDetailed import SynchronousMachineDetailed


@dataclass(config=DataclassConfig)
class SynchronousMachineTimeConstantReactance(SynchronousMachineDetailed):
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

    rotorType: Optional[str] = None  # Type M:0..1 in CIM
    modelType: Optional[str] = None  # Type M:1..1 in CIM
    ks: float = 0.0  # Type #Float in CIM
    xDirectSync: float = 0.0  # Type #PU in CIM
    xDirectTrans: float = 0.0  # Type #PU in CIM
    xDirectSubtrans: float = 0.0  # Type #PU in CIM
    xQuadSync: float = 0.0  # Type #PU in CIM
    xQuadTrans: float = 0.0  # Type #PU in CIM
    xQuadSubtrans: float = 0.0  # Type #PU in CIM
    tpdo: int = 0  # Type #Seconds in CIM
    tppdo: int = 0  # Type #Seconds in CIM
    tpqo: int = 0  # Type #Seconds in CIM
    tppqo: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=SynchronousMachineTimeConstantReactance"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.DY.value,
            ],
            # Attributes
            "rotorType": [
                Profile.DY.value,
            ],
            "modelType": [
                Profile.DY.value,
            ],
            "ks": [
                Profile.DY.value,
            ],
            "xDirectSync": [
                Profile.DY.value,
            ],
            "xDirectTrans": [
                Profile.DY.value,
            ],
            "xDirectSubtrans": [
                Profile.DY.value,
            ],
            "xQuadSync": [
                Profile.DY.value,
            ],
            "xQuadTrans": [
                Profile.DY.value,
            ],
            "xQuadSubtrans": [
                Profile.DY.value,
            ],
            "tpdo": [
                Profile.DY.value,
            ],
            "tppdo": [
                Profile.DY.value,
            ],
            "tpqo": [
                Profile.DY.value,
            ],
            "tppqo": [
                Profile.DY.value,
            ],
            "tc": [
                Profile.DY.value,
            ],
        }
