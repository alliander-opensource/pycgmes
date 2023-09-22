"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .Equipment import Equipment


@dataclass(config=DataclassConfig)
class AuxiliaryEquipment(Equipment, ModuleType):
    """
    AuxiliaryEquipment describe equipment that is not performing any primary functions but support for the equipment
      performing the primary function. AuxiliaryEquipment is attached to primary equipment via an association with
      Terminal.

    Terminal: The Terminal at the equipment where the AuxiliaryEquipment is attached.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return AuxiliaryEquipment(*args, **kwargs)

    Terminal: Optional[str] = Field(
        default=None,
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
# "import AuxiliaryEquipment"
# work as well as
# "from AuxiliaryEquipment import AuxiliaryEquipment".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = AuxiliaryEquipment
