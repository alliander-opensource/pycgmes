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

from ..utils.base import Base


@dataclass(config=DataclassConfig)
class SvPowerFlow(Base, ModuleType):
    """
    State variable for power flow. Load convention is used for flow direction. This means flow out from the
      TopologicalNode into the equipment is positive.

    p: The active power flow. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode
      (bus) into the conducting equipment.
    q: The reactive power flow. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode
      (bus) into the conducting equipment.
    Terminal: The terminal associated with the power flow state variable.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return SvPowerFlow(*args, **kwargs)

    p: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SV,
        ],
    )

    q: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SV,
        ],
    )

    Terminal: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SV,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.SV,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import SvPowerFlow"
# work as well as
# "from SvPowerFlow import SvPowerFlow".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = SvPowerFlow
