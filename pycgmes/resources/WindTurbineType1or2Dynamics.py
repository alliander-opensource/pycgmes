"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass
class WindTurbineType1or2Dynamics(DynamicsFunctionBlock):
    """
    Parent class supporting relationships to wind turbines type 1 and type 2 and their control models.  Generator model
      for wind turbine of type 1 or type 2 is a standard asynchronous generator model.

    RemoteInputSignal: Remote input signal used by this wind generator type 1 or type 2 model.
    AsynchronousMachineDynamics: Asynchronous machine model with which this wind generator type 1 or type 2 model is
      associated.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    RemoteInputSignal: Optional[str] = None  # Type M:0..1 in CIM
    AsynchronousMachineDynamics: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindTurbineType1or2Dynamics\n"
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
            "RemoteInputSignal": [
                self.profiles.DY.value,
            ],
            "AsynchronousMachineDynamics": [
                self.profiles.DY.value,
            ],
        }
