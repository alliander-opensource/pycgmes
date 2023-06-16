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
class WindPlantDynamics(DynamicsFunctionBlock):
    """
    Parent class supporting relationships to wind turbines type 3 and type 4 and wind plant IEC and user-defined wind
      plants including their control models.

    RemoteInputSignal: The remote signal with which this power plant is associated.
    WindTurbineType3or4Dynamics: The wind turbine type 3 or type 4 associated with this wind plant.
    """

    RemoteInputSignal: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # WindTurbineType3or4Dynamics : list = field(default_factory=list)  # Type M:1..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindPlantDynamics"]
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
            "WindTurbineType3or4Dynamics": [
                Profile.DY.value,
            ],
        }
