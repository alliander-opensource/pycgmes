"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .RotatingMachineDynamics import RotatingMachineDynamics


@dataclass(config=DataclassConfig)
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

    AsynchronousMachine: Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # TurbineGovernorDynamics : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # MechanicalLoadDynamics : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # WindTurbineType1or2Dynamics : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=AsynchronousMachineDynamics"]
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
            "AsynchronousMachine": [
                Profile.DY.value,
            ],
            "TurbineGovernorDynamics": [
                Profile.DY.value,
            ],
            "MechanicalLoadDynamics": [
                Profile.DY.value,
            ],
            "WindTurbineType1or2Dynamics": [
                Profile.DY.value,
            ],
        }
