"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .RotatingMachineDynamics import RotatingMachineDynamics


@dataclass
class AsynchronousMachineDynamics(RotatingMachineDynamics):
    """
    Asynchronous machine whose behaviour is described by reference to a standard model expressed in either time constant
      reactance form or equivalent circuit form or by definition of a user-defined model. Parameter details:
      Asynchronous machine parameters such as Xl, Xs, etc. are actually used as inductances in the model, but are
      commonly referred to as reactances since, at nominal frequency, the PU values are the same. However, some
      references use the symbol L instead of X.

    AsynchronousMachine: Asynchronous machine to which this asynchronous machine dynamics model applies.
    TurbineGovernorDynamics: Turbine-governor model associated with this asynchronous machine model.
    MechanicalLoadDynamics: Mechanical load model associated with this asynchronous machine model.
    WindTurbineType1or2Dynamics: Wind generator type 1 or type 2 model associated with this asynchronous machine model.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    AsynchronousMachine: Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # TurbineGovernorDynamics : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # MechanicalLoadDynamics : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # WindTurbineType1or2Dynamics : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=AsynchronousMachineDynamics\n"
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
            "AsynchronousMachine": [
                self.profiles.DY.value,
            ],
            "TurbineGovernorDynamics": [
                self.profiles.DY.value,
            ],
            "MechanicalLoadDynamics": [
                self.profiles.DY.value,
            ],
            "WindTurbineType1or2Dynamics": [
                self.profiles.DY.value,
            ],
        }
