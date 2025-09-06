"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .SynchronousMachineDetailed import SynchronousMachineDetailed


@dataclass
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

    ks: Saturation loading correction factor (Ks) (>= 0).  Used only by type J model.  Typical value = 0.
    modelType: Type of synchronous machine model used in dynamic simulation applications.
    rotorType: Type of rotor on physical machine.
    tc: Damping time constant for `Canay` reactance (>= 0).  Typical value = 0.
    tpdo: Direct-axis transient rotor time constant (T`do) (> SynchronousMachineTimeConstantReactance.tppdo).  Typical
      value = 5.
    tppdo: Direct-axis subtransient rotor time constant (T``do) (> 0).  Typical value = 0,03.
    tppqo: Quadrature-axis subtransient rotor time constant (T``qo) (> 0). Typical value = 0,03.
    tpqo: Quadrature-axis transient rotor time constant (T`qo) (> SynchronousMachineTimeConstantReactance.tppqo).
      Typical value = 0,5.
    xDirectSubtrans: Direct-axis subtransient reactance (unsaturated) (X``d) (>
      RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2.
    xDirectSync: Direct-axis synchronous reactance (Xd) (>= SynchronousMachineTimeConstantReactance.xDirectTrans). The
      quotient of a sustained value of that AC component of armature voltage that is produced by the
      total direct-axis flux due to direct-axis armature current and the value of the AC component of
      this current, the machine running at rated speed.  Typical value = 1,8.
    xDirectTrans: Direct-axis transient reactance (unsaturated) (X`d) (>=
      SynchronousMachineTimeConstantReactance.xDirectSubtrans).  Typical value = 0,5.
    xQuadSubtrans: Quadrature-axis subtransient reactance (X``q) (> RotatingMachineDynamics.statorLeakageReactance).
      Typical value = 0,2.
    xQuadSync: Quadrature-axis synchronous reactance (Xq) (>= SynchronousMachineTimeConstantReactance.xQuadTrans). The
      ratio of the component of reactive armature voltage, due to the quadrature-axis component of
      armature current, to this component of current, under steady state conditions and at rated
      frequency.  Typical value = 1,6.
    xQuadTrans: Quadrature-axis transient reactance (X`q) (>= SynchronousMachineTimeConstantReactance.xQuadSubtrans).
      Typical value = 0,3.
    """

    ks: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Float",
        },
    )

    modelType: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": True,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    rotorType: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": True,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    tc: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "Seconds",
        },
    )

    tpdo: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "Seconds",
        },
    )

    tppdo: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "Seconds",
        },
    )

    tppqo: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "Seconds",
        },
    )

    tpqo: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "Seconds",
        },
    )

    xDirectSubtrans: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "PU",
        },
    )

    xDirectSync: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "PU",
        },
    )

    xDirectTrans: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "PU",
        },
    )

    xQuadSubtrans: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "PU",
        },
    )

    xQuadSync: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "PU",
        },
    )

    xQuadTrans: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "PU",
        },
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

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.DY
