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
class TurbineGovernorDynamics(DynamicsFunctionBlock):
    """
    Turbine-governor function block whose behaviour is described by reference to a standard model or by definition of a
      user-defined model.

    SynchronousMachineDynamics: Synchronous machine model with which this turbine-governor model is associated.
      TurbineGovernorDynamics shall have either an association to
      SynchronousMachineDynamics or to AsynchronousMachineDynamics.
    AsynchronousMachineDynamics: Asynchronous machine model with which this turbine-governor model is associated.
      TurbineGovernorDynamics shall have either an association to
      SynchronousMachineDynamics or to AsynchronousMachineDynamics.
    TurbineLoadControllerDynamics: Turbine load controller providing input to this turbine-governor.
    """

    SynchronousMachineDynamics: Optional[str] = None  # Type M:0..1 in CIM
    AsynchronousMachineDynamics: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # TurbineLoadControllerDynamics : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=TurbineGovernorDynamics"]
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
            "AsynchronousMachineDynamics": [
                Profile.DY.value,
            ],
            "TurbineLoadControllerDynamics": [
                Profile.DY.value,
            ],
        }
