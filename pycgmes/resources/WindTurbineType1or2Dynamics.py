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
class WindTurbineType1or2Dynamics(DynamicsFunctionBlock):
    """
    Parent class supporting relationships to wind turbines type 1 and type 2 and their control models.  Generator model
      for wind turbine of type 1 or type 2 is a standard asynchronous generator model.

    RemoteInputSignal: Remote input signal used by this wind generator type 1 or type 2 model.
    AsynchronousMachineDynamics: Asynchronous machine model with which this wind generator type 1 or type 2 model is
      associated.
    """

    RemoteInputSignal: Optional[str] = None  # Type M:0..1 in CIM
    AsynchronousMachineDynamics: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindTurbineType1or2Dynamics"]
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
            "RemoteInputSignal": [
                Profile.DY.value,
            ],
            "AsynchronousMachineDynamics": [
                Profile.DY.value,
            ],
        }
