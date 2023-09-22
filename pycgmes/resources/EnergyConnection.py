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
class EnergyConnection(ConductingEquipment, ModuleType):
    """
    A connection of energy generation or consumption on the power system model.

    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return EnergyConnection(*args, **kwargs)

    # No attributes defined for this class.

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SC,
            Profile.SSH,
            Profile.DY,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import EnergyConnection"
# work as well as
# "from EnergyConnection import EnergyConnection".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = EnergyConnection
