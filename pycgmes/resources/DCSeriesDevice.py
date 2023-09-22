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
class DCSeriesDevice(DCConductingEquipment, ModuleType):
    """
    A series device within the DC system, typically a reactor used for filtering or smoothing.  Needed for transient and
      short circuit studies.

    inductance: Inductance of the device.
    resistance: Resistance of the DC device.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return DCSeriesDevice(*args, **kwargs)

    inductance: float = Field(
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
# "import DCSeriesDevice"
# work as well as
# "from DCSeriesDevice import DCSeriesDevice".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = DCSeriesDevice
