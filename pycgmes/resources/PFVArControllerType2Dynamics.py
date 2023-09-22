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
class PFVArControllerType2Dynamics(DynamicsFunctionBlock, ModuleType):
    """
    Power factor or VAr controller type 2 function block whose behaviour is described by reference to a standard model
      or by definition of a user-defined model.

    ExcitationSystemDynamics: Excitation system model with which this power factor or VAr controller type 2 is
      associated.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return PFVArControllerType2Dynamics(*args, **kwargs)

    ExcitationSystemDynamics: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

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
# "import PFVArControllerType2Dynamics"
# work as well as
# "from PFVArControllerType2Dynamics import PFVArControllerType2Dynamics".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = PFVArControllerType2Dynamics
