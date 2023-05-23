"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass
class PFVArControllerType2Dynamics(DynamicsFunctionBlock):
    """
    Power factor or VAr controller type 2 function block whose behaviour is described by reference to a standard model
      or by definition of a user-defined model.

    ExcitationSystemDynamics: Excitation system model with which this power factor or VAr controller type 2 is
      associated.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ExcitationSystemDynamics: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PFVArControllerType2Dynamics\n"
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
            "ExcitationSystemDynamics": [
                self.profiles.DY.value,
            ],
        }
