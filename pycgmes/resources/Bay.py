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

from .EquipmentContainer import EquipmentContainer


@dataclass(config=DataclassConfig)
class Bay(EquipmentContainer, ModuleType):
    """
    A collection of power system resources (within a given substation) including conducting equipment, protection
      relays, measurements, and telemetry.  A bay typically represents a physical grouping related to modularization
      of equipment.

    VoltageLevel: The voltage level containing this bay.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return Bay(*args, **kwargs)

    VoltageLevel: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQBD,
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
            Profile.EQBD,
            Profile.EQ,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import Bay"
# work as well as
# "from Bay import Bay".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = Bay
