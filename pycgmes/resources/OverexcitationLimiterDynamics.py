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
class OverexcitationLimiterDynamics(DynamicsFunctionBlock, ModuleType):
    """
    Overexcitation limiter function block whose behaviour is described by reference to a standard model or by definition
      of a user-defined model.

    ExcitationSystemDynamics: Excitation system model with which this overexcitation limiter model is associated.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return OverexcitationLimiterDynamics(*args, **kwargs)

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
# "import OverexcitationLimiterDynamics"
# work as well as
# "from OverexcitationLimiterDynamics import OverexcitationLimiterDynamics".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = OverexcitationLimiterDynamics
