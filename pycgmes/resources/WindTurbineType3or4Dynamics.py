"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass
class WindTurbineType3or4Dynamics(DynamicsFunctionBlock):
    """
    Parent class supporting relationships to wind turbines type 3 and type 4 and wind plant including their control
      models.

    PowerElectronicsConnection: The power electronics connection associated with this wind turbine type 3 or type 4
      dynamics model.
    RemoteInputSignal: Remote input signal used by these wind turbine type 3 or type 4 models.
    WindPlantDynamics: The wind plant with which the wind turbines type 3 or type 4 are associated.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    PowerElectronicsConnection: Optional[str] = None  # Type M:1 in CIM
    RemoteInputSignal: Optional[str] = None  # Type M:0..1 in CIM
    WindPlantDynamics: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindTurbineType3or4Dynamics\n"
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
            "PowerElectronicsConnection": [
                self.profiles.DY.value,
            ],
            "RemoteInputSignal": [
                self.profiles.DY.value,
            ],
            "WindPlantDynamics": [
                self.profiles.DY.value,
            ],
        }
