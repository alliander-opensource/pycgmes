"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass(config=DataclassConfig)
class ExcitationSystemDynamics(DynamicsFunctionBlock):
    """
    Excitation system function block whose behaviour is described by reference to a standard model or by definition of a
      user-defined model.

    SynchronousMachineDynamics: Synchronous machine model with which this excitation system model is associated.
    VoltageCompensatorDynamics: Voltage compensator model associated with this excitation system model.
    OverexcitationLimiterDynamics: Overexcitation limiter model associated with this excitation system model.
    PFVArControllerType2Dynamics: Power factor or VAr controller type 2 model associated with this excitation system
      model.
    DiscontinuousExcitationControlDynamics: Discontinuous excitation control model associated with this excitation
      system model.
    PowerSystemStabilizerDynamics: Power system stabilizer model associated with this excitation system model.
    UnderexcitationLimiterDynamics: Undrexcitation limiter model associated with this excitation system model.
    PFVArControllerType1Dynamics: Power factor or VAr controller type 1 model associated with this excitation system
      model.
    """

    SynchronousMachineDynamics: Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # VoltageCompensatorDynamics : Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # OverexcitationLimiterDynamics : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # PFVArControllerType2Dynamics : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # DiscontinuousExcitationControlDynamics : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # PowerSystemStabilizerDynamics : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # UnderexcitationLimiterDynamics : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # PFVArControllerType1Dynamics : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcitationSystemDynamics"]
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
            "SynchronousMachineDynamics": [
                Profile.DY.value,
            ],
            "VoltageCompensatorDynamics": [
                Profile.DY.value,
            ],
            "OverexcitationLimiterDynamics": [
                Profile.DY.value,
            ],
            "PFVArControllerType2Dynamics": [
                Profile.DY.value,
            ],
            "DiscontinuousExcitationControlDynamics": [
                Profile.DY.value,
            ],
            "PowerSystemStabilizerDynamics": [
                Profile.DY.value,
            ],
            "UnderexcitationLimiterDynamics": [
                Profile.DY.value,
            ],
            "PFVArControllerType1Dynamics": [
                Profile.DY.value,
            ],
        }
