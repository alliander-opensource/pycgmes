"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .OperationalLimit import OperationalLimit


@dataclass(config=DataclassConfig)
class VoltageLimit(OperationalLimit, ModuleType):
    """
    Operational limit applied to voltage. The use of operational VoltageLimit is preferred instead of limits defined at
      VoltageLevel. The operational VoltageLimits are used, if present.

    normalValue: The normal limit on voltage. High or low limit nature of the limit depends upon the properties of the
      operational limit type. The attribute shall be a positive value or zero.
    value: Limit on voltage. High or low limit nature of the limit depends upon the properties of the operational limit
      type. The attribute shall be a positive value or zero.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return VoltageLimit(*args, **kwargs)

    normalValue: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    value: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
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
            Profile.SSH,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import VoltageLimit"
# work as well as
# "from VoltageLimit import VoltageLimit".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = VoltageLimit
