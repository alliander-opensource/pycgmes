"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .PhaseTapChangerNonLinear import PhaseTapChangerNonLinear


@dataclass(config=DataclassConfig)
class PhaseTapChangerSymmetrical(PhaseTapChangerNonLinear, ModuleType):
    """
    Describes a symmetrical phase shifting transformer tap model in which the voltage magnitude of both sides is the
      same. The difference voltage magnitude is the base in an equal-sided triangle where the sides corresponds to
      the primary and secondary voltages. The phase angle difference corresponds to the top angle and can be
      expressed as twice the arctangent of half the total difference voltage.

    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return PhaseTapChangerSymmetrical(*args, **kwargs)

    # No attributes defined for this class.

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
# "import PhaseTapChangerSymmetrical"
# work as well as
# "from PhaseTapChangerSymmetrical import PhaseTapChangerSymmetrical".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = PhaseTapChangerSymmetrical
