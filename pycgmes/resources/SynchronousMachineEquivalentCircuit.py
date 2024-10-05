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
class SynchronousMachineEquivalentCircuit(SynchronousMachineDetailed):
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

    r1d: Direct-axis damper 1 winding resistance.
    r1q: Quadrature-axis damper 1 winding resistance.
    r2q: Quadrature-axis damper 2 winding resistance.
    rfd: Field winding resistance.
    x1d: Direct-axis damper 1 winding leakage reactance.
    x1q: Quadrature-axis damper 1 winding leakage reactance.
    x2q: Quadrature-axis damper 2 winding leakage reactance.
    xad: Direct-axis mutual reactance.
    xaq: Quadrature-axis mutual reactance.
    xf1d: Differential mutual (`Canay`) reactance.
    xfd: Field winding leakage reactance.
    """

    r1d: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    r1q: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    r2q: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    rfd: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    x1d: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    x1q: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    x2q: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    xad: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    xaq: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    xf1d: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    xfd: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
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
