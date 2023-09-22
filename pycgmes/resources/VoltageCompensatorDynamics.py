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
class VoltageCompensatorDynamics(DynamicsFunctionBlock, ModuleType):
    """
    Voltage compensator function block whose behaviour is described by reference to a standard model or by definition of
      a user-defined model.

    RemoteInputSignal: Remote input signal used by this voltage compensator model.
    ExcitationSystemDynamics: Excitation system model with which this voltage compensator is associated.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return VoltageCompensatorDynamics(*args, **kwargs)

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # RemoteInputSignal : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

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
# "import VoltageCompensatorDynamics"
# work as well as
# "from VoltageCompensatorDynamics import VoltageCompensatorDynamics".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = VoltageCompensatorDynamics
