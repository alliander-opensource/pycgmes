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

from .EquivalentEquipment import EquivalentEquipment


@dataclass(config=DataclassConfig)
class EquivalentShunt(EquivalentEquipment, ModuleType):
    """
    The class represents equivalent shunts.

    b: Positive sequence shunt susceptance.
    g: Positive sequence shunt conductance.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return EquivalentShunt(*args, **kwargs)

    b: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    g: float = Field(
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
# "import EquivalentShunt"
# work as well as
# "from EquivalentShunt import EquivalentShunt".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = EquivalentShunt
