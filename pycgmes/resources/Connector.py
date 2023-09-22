"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .ConductingEquipment import ConductingEquipment


@dataclass(config=DataclassConfig)
class Connector(ConductingEquipment, ModuleType):
    """
    A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment
      within a single substation and are modelled with a single logical terminal.

    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return Connector(*args, **kwargs)

    # No attributes defined for this class.

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQBD,
            Profile.EQ,
            Profile.SC,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import Connector"
# work as well as
# "from Connector import Connector".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = Connector
