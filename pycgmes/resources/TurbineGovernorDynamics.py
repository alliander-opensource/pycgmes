"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass(config=DataclassConfig)
class TurbineGovernorDynamics(DynamicsFunctionBlock, ModuleType):
    """
    Turbine-governor function block whose behaviour is described by reference to a standard model or by definition of a
      user-defined model.

    SynchronousMachineDynamics: Synchronous machine model with which this turbine-governor model is associated.
      TurbineGovernorDynamics shall have either an association to
      SynchronousMachineDynamics or to AsynchronousMachineDynamics.
    AsynchronousMachineDynamics: Asynchronous machine model with which this turbine-governor model is associated.
      TurbineGovernorDynamics shall have either an association to
      SynchronousMachineDynamics or to AsynchronousMachineDynamics.
    TurbineLoadControllerDynamics: Turbine load controller providing input to this turbine-governor.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return TurbineGovernorDynamics(*args, **kwargs)

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

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # TurbineLoadControllerDynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import TurbineGovernorDynamics"
# work as well as
# "from TurbineGovernorDynamics import TurbineGovernorDynamics".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = TurbineGovernorDynamics
