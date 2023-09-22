"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class Limit(IdentifiedObject, ModuleType):
    """
    Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by
      the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit
      or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may
      indicate both meaning and use.

    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return Limit(*args, **kwargs)

    # No attributes defined for this class.

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
# "import Limit"
# work as well as
# "from Limit import Limit".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = Limit
