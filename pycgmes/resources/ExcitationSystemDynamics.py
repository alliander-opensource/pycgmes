"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass(config=DataclassConfig)
class ExcitationSystemDynamics(DynamicsFunctionBlock):
    """
    Excitation system function block whose behaviour is described by reference to a standard model or by definition of a
      user-defined model.

    SynchronousMachineDynamics: Synchronous machine model with which this excitation system model is associated.
    VoltageCompensatorDynamics: Voltage compensator model associated with this excitation system model.
    OverexcitationLimiterDynamics: Overexcitation limiter model associated with this excitation system model.
    PFVArControllerType2Dynamics: Power factor or VAr controller type 2 model associated with this excitation system
      model.
    DiscontinuousExcitationControlDynamics: Discontinuous excitation control model associated with this excitation
      system model.
    PowerSystemStabilizerDynamics: Power system stabilizer model associated with this excitation system model.
    UnderexcitationLimiterDynamics: Undrexcitation limiter model associated with this excitation system model.
    PFVArControllerType1Dynamics: Power factor or VAr controller type 1 model associated with this excitation system
      model.
    """

    SynchronousMachineDynamics: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:1 in CIM  # pylint: disable-next=line-too-long
    # VoltageCompensatorDynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # OverexcitationLimiterDynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # PFVArControllerType2Dynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # DiscontinuousExcitationControlDynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ]) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # PowerSystemStabilizerDynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # UnderexcitationLimiterDynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # PFVArControllerType1Dynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
