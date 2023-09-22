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

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class TieFlow(IdentifiedObject, ModuleType):
    """
    Defines the structure (in terms of location and direction) of the net interchange constraint for a control area.
      This constraint may be used by either AGC or power flow.

    ControlArea: The control area of the tie flows.
    Terminal: The terminal to which this tie flow belongs.
    positiveFlowIn: Specifies the sign of the tie flow associated with a control area. True if positive flow into the
      terminal (load convention) is also positive flow into the control area.  See the description
      of ControlArea for further explanation of how TieFlow.positiveFlowIn is used.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return TieFlow(*args, **kwargs)

    ControlArea: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    Terminal: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    positiveFlowIn: bool = Field(
        default=False,
        in_profiles=[
            Profile.EQ,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import TieFlow"
# work as well as
# "from TieFlow import TieFlow".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = TieFlow
