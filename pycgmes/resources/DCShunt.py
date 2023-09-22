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

from .DCConductingEquipment import DCConductingEquipment


@dataclass(config=DataclassConfig)
class DCShunt(DCConductingEquipment, ModuleType):
    """
    A shunt device within the DC system, typically used for filtering.  Needed for transient and short circuit studies.

    capacitance: Capacitance of the DC shunt.
    resistance: Resistance of the DC device.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return DCShunt(*args, **kwargs)

    capacitance: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    resistance: float = Field(
        default=0.0,
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
# "import DCShunt"
# work as well as
# "from DCShunt import DCShunt".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = DCShunt
