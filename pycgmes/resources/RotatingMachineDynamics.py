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

from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass(config=DataclassConfig)
class RotatingMachineDynamics(DynamicsFunctionBlock, ModuleType):
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

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return RotatingMachineDynamics(*args, **kwargs)

    damping: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    inertia: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    saturationFactor: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    saturationFactor120: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    statorLeakageReactance: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    statorResistance: float = Field(
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
# "import RotatingMachineDynamics"
# work as well as
# "from RotatingMachineDynamics import RotatingMachineDynamics".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = RotatingMachineDynamics
