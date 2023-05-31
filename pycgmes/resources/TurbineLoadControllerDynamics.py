"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass
class TurbineLoadControllerDynamics(DynamicsFunctionBlock):
    """
    Turbine load controller function block whose behaviour is described by reference to a standard model or by
      definition of a user-defined model.

    TurbineGovernorDynamics: Turbine-governor controlled by this turbine load controller.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    TurbineGovernorDynamics: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=TurbineLoadControllerDynamics\n"
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
            "TurbineGovernorDynamics": [
                self.profiles.DY.value,
            ],
        }
