"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass(config=DataclassConfig)
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

    damping: float = 0.0  # Type #Float in CIM
    inertia: int = 0  # Type #Seconds in CIM
    saturationFactor: float = 0.0  # Type #Float in CIM
    saturationFactor120: float = 0.0  # Type #Float in CIM
    statorLeakageReactance: float = 0.0  # Type #PU in CIM
    statorResistance: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=RotatingMachineDynamics"]
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
            "damping": [
                Profile.DY.value,
            ],
            "inertia": [
                Profile.DY.value,
            ],
            "saturationFactor": [
                Profile.DY.value,
            ],
            "saturationFactor120": [
                Profile.DY.value,
            ],
            "statorLeakageReactance": [
                Profile.DY.value,
            ],
            "statorResistance": [
                Profile.DY.value,
            ],
        }
