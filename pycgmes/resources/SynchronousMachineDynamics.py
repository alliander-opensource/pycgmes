"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

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

    SynchronousMachine: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # CrossCompoundTurbineGovernorDyanmics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ]) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # CrossCompoundTurbineGovernorDynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ]) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # MechanicalLoadDynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # ExcitationSystemDynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # TurbineGovernorDynamics : list = Field(default_factory=list, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # GenICompensationForGenJ : list = Field(default_factory=list, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
