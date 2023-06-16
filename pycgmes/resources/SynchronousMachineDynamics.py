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
class SynchronousMachineDynamics(RotatingMachineDynamics):
    """
    Synchronous machine whose behaviour is described by reference to a standard model expressed in one of the following
      forms: - simplified (or classical), where a group of generators or motors is not modelled in detail; -
      detailed, in equivalent circuit form; - detailed, in time constant reactance form; or - by definition of a
      user-defined model. It is a common practice to represent small generators by a negative load rather than by a
      dynamic generator model when performing dynamics simulations. In this case, a SynchronousMachine in the static
      model is not represented by anything in the dynamics model, instead it is treated as an ordinary load.
      Parameter details:  Synchronous machine parameters such as Xl, Xd, Xp etc. are actually used as inductances in
      the models, but are commonly referred to as reactances since, at nominal frequency, the PU values are the
      same. However, some references use the symbol L instead of X.

    SynchronousMachine: Synchronous machine to which synchronous machine dynamics model applies.
    CrossCompoundTurbineGovernorDyanmics: The cross-compound turbine governor with which this high-pressure synchronous
      machine is associated.
    CrossCompoundTurbineGovernorDynamics: The cross-compound turbine governor with which this low-pressure synchronous
      machine is associated.
    MechanicalLoadDynamics: Mechanical load model associated with this synchronous machine model.
    ExcitationSystemDynamics: Excitation system model associated with this synchronous machine model.
    TurbineGovernorDynamics: Turbine-governor model associated with this synchronous machine model. Multiplicity of
      greater than one is intended to support hydro units that have multiple turbines on
      one generator.
    GenICompensationForGenJ: Compensation of voltage compensator`s generator for current flow out of this  generator.
    """

    SynchronousMachine: Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # CrossCompoundTurbineGovernorDyanmics : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # CrossCompoundTurbineGovernorDynamics : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # MechanicalLoadDynamics : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # ExcitationSystemDynamics : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # TurbineGovernorDynamics : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # GenICompensationForGenJ : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=SynchronousMachineDynamics"]
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
            "SynchronousMachine": [
                Profile.DY.value,
            ],
            "CrossCompoundTurbineGovernorDyanmics": [
                Profile.DY.value,
            ],
            "CrossCompoundTurbineGovernorDynamics": [
                Profile.DY.value,
            ],
            "MechanicalLoadDynamics": [
                Profile.DY.value,
            ],
            "ExcitationSystemDynamics": [
                Profile.DY.value,
            ],
            "TurbineGovernorDynamics": [
                Profile.DY.value,
            ],
            "GenICompensationForGenJ": [
                Profile.DY.value,
            ],
        }
