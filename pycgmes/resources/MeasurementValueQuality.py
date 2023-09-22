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

from .Quality61850 import Quality61850


@dataclass(config=DataclassConfig)
class MeasurementValueQuality(Quality61850, ModuleType):
    """
    Measurement quality flags. Bits 0-10 are defined for substation automation in IEC 61850-7-3. Bits 11-15 are reserved
      for future expansion by that document. Bits 16-31 are reserved for EMS applications.

    MeasurementValue: A MeasurementValue has a MeasurementValueQuality associated with it.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return MeasurementValueQuality(*args, **kwargs)

    MeasurementValue: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import MeasurementValueQuality"
# work as well as
# "from MeasurementValueQuality import MeasurementValueQuality".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = MeasurementValueQuality
