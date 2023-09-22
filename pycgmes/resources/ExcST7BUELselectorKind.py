"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from ..utils.base import Base


@dataclass(config=DataclassConfig)
class ExcST7BUELselectorKind(Base, ModuleType):
    """
    Types of connections for the UEL input used for static excitation systems type 7B.

    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ExcST7BUELselectorKind(*args, **kwargs)

    # No attributes defined for this class.

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
# "import ExcST7BUELselectorKind"
# work as well as
# "from ExcST7BUELselectorKind import ExcST7BUELselectorKind".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ExcST7BUELselectorKind
