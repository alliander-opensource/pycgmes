"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .RotatingMachineDynamics import RotatingMachineDynamics


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=SynchronousMachineDynamics\n"
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
            "SynchronousMachine": [
                self.profiles.DY.value,
            ],
            "CrossCompoundTurbineGovernorDyanmics": [
                self.profiles.DY.value,
            ],
            "CrossCompoundTurbineGovernorDynamics": [
                self.profiles.DY.value,
            ],
            "MechanicalLoadDynamics": [
                self.profiles.DY.value,
            ],
            "ExcitationSystemDynamics": [
                self.profiles.DY.value,
            ],
            "TurbineGovernorDynamics": [
                self.profiles.DY.value,
            ],
            "GenICompensationForGenJ": [
                self.profiles.DY.value,
            ],
        }
