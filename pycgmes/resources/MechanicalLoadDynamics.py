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
class MechanicalLoadDynamics(DynamicsFunctionBlock):
    """
    Mechanical load function block whose behaviour is described by reference to a standard model or by definition of a
      user-defined model.

    SynchronousMachineDynamics: Synchronous machine model with which this mechanical load model is associated.
      MechanicalLoadDynamics shall have either an association to
      SynchronousMachineDynamics or AsynchronousMachineDyanmics.
    AsynchronousMachineDynamics: Asynchronous machine model with which this mechanical load model is associated.
      MechanicalLoadDynamics shall have either an association to
      SynchronousMachineDynamics or to AsynchronousMachineDynamics.
    """

    SynchronousMachineDynamics: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    AsynchronousMachineDynamics: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
