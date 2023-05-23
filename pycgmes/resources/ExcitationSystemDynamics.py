"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=ExcitationSystemDynamics\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.DY.value,
            ],
            # Attributes
            "SynchronousMachineDynamics": [
                self.profiles.DY.value,
            ],
            "VoltageCompensatorDynamics": [
                self.profiles.DY.value,
            ],
            "OverexcitationLimiterDynamics": [
                self.profiles.DY.value,
            ],
            "PFVArControllerType2Dynamics": [
                self.profiles.DY.value,
            ],
            "DiscontinuousExcitationControlDynamics": [
                self.profiles.DY.value,
            ],
            "PowerSystemStabilizerDynamics": [
                self.profiles.DY.value,
            ],
            "UnderexcitationLimiterDynamics": [
                self.profiles.DY.value,
            ],
            "PFVArControllerType1Dynamics": [
                self.profiles.DY.value,
            ],
        }
