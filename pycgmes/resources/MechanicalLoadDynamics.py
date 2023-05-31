"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass
class MechanicalLoadDynamics(DynamicsFunctionBlock):
    """
    Mechanical load function block whose behaviour is described by reference to a standard model or by definition of a
      user-defined model.

    SynchronousMachineDynamics: Synchronous machine model with which this mechanical load model is associated.
      MechanicalLoadDynamics shall have either an association to
      SynchronousMachineDynamics or AsynchronousMachineDyanmics.
    AsynchronousMachineDynamics: Asynchronous machine model with which this mechanical load model is associated.
      MechanicalLoadDynamics shall have either an association to
      SynchronousMachineDynamics or to AsynchronousMachineDynamics.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    SynchronousMachineDynamics: Optional[str] = None  # Type M:0..1 in CIM
    AsynchronousMachineDynamics: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=MechanicalLoadDynamics\n"
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
            "AsynchronousMachineDynamics": [
                self.profiles.DY.value,
            ],
        }
