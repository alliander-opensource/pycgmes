"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .Switch import Switch


@dataclass(config=DataclassConfig)
class Jumper(Switch, ModuleType):
    """
    A short section of conductor with negligible impedance which can be manually removed and replaced if the circuit is
      de-energized. Note that zero-impedance branches can potentially be modelled by other equipment types.

    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return Jumper(*args, **kwargs)

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
# "import Jumper"
# work as well as
# "from Jumper import Jumper".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = Jumper
