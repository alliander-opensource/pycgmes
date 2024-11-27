"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass
class RotatingMachineDynamics(DynamicsFunctionBlock):
    """
    Abstract parent class for all synchronous and asynchronous machine standard models.

    damping: Damping torque coefficient (D) (>= 0).  A proportionality constant that, when multiplied by the angular
      velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping
      torque.  This value is often zero when the sources of damping torques (generator damper windings,
      load damping effects, etc.) are modelled in detail.  Typical value = 0.
    inertia: Inertia constant of generator or motor and mechanical load (H) (> 0).  This is the specification for the
      stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the
      generator plus all other elements (turbine, exciter) on the same shaft and has units of MW x s.  For
      a motor, it includes the motor plus its mechanical load. Conventional units are PU on the generator
      MVA base, usually expressed as MW x s / MVA or just s. This value is used in the accelerating power
      reference frame for operator training simulator solutions.  Typical value = 3.
    saturationFactor: Saturation factor at rated terminal voltage (S1) (>= 0).  Not used by simplified model.  Defined
      by defined by S(E1) in the SynchronousMachineSaturationParameters diagram.  Typical value =
      0,02.
    saturationFactor120: Saturation factor at 120% of rated terminal voltage (S12) (>=
      RotatingMachineDynamics.saturationFactor). Not used by the simplified model, defined by
      S(E2) in the SynchronousMachineSaturationParameters diagram.  Typical value = 0,12.
    statorLeakageReactance: Stator leakage reactance (Xl) (>= 0). Typical value = 0,15.
    statorResistance: Stator (armature) resistance (Rs) (>= 0). Typical value = 0,005.
    """

    damping: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Float",
        },
    )

    inertia: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "Seconds",
        },
    )

    saturationFactor: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Float",
        },
    )

    saturationFactor120: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Float",
        },
    )

    statorLeakageReactance: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "PU",
        },
    )

    statorResistance: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
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
