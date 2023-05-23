"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass
class PowerSystemStabilizerDynamics(DynamicsFunctionBlock):
    """
    Power system stabilizer function block whose behaviour is described by reference to a standard model or by
      definition of a user-defined model.

    RemoteInputSignal: Remote input signal used by this power system stabilizer model.
    ExcitationSystemDynamics: Excitation system model with which this power system stabilizer model is associated.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # RemoteInputSignal : list = field(default_factory=list)  # Type M:0..n in CIM
    ExcitationSystemDynamics: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PowerSystemStabilizerDynamics\n"
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
            "ExcitationSystemDynamics": [
                self.profiles.DY.value,
            ],
        }
