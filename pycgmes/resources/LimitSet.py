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

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class LimitSet(IdentifiedObject, ModuleType):
    """
    Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets
      corresponding to seasonal or other changing conditions. The condition is captured in the name and description
      attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used
      this way.

    isPercentageLimits: Tells if the limit values are in percentage of normalValue or the specified Unit for
      Measurements and Controls.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return LimitSet(*args, **kwargs)

    isPercentageLimits: bool = Field(
        default=False,
        in_profiles=[
            Profile.OP,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import LimitSet"
# work as well as
# "from LimitSet import LimitSet".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = LimitSet
