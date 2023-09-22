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
class WindTurbineType1or2Dynamics(DynamicsFunctionBlock, ModuleType):
    """
    Parent class supporting relationships to wind turbines type 1 and type 2 and their control models.  Generator model
      for wind turbine of type 1 or type 2 is a standard asynchronous generator model.

    RemoteInputSignal: Remote input signal used by this wind generator type 1 or type 2 model.
    AsynchronousMachineDynamics: Asynchronous machine model with which this wind generator type 1 or type 2 model is
      associated.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return WindTurbineType1or2Dynamics(*args, **kwargs)

    RemoteInputSignal: Optional[str] = Field(
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
# "import WindTurbineType1or2Dynamics"
# work as well as
# "from WindTurbineType1or2Dynamics import WindTurbineType1or2Dynamics".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = WindTurbineType1or2Dynamics
