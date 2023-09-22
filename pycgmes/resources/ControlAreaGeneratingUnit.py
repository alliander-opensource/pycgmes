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

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class ControlAreaGeneratingUnit(IdentifiedObject, ModuleType):
    """
    A control area generating unit. This class is needed so that alternate control area definitions may include the same
      generating unit.   It should be noted that only one instance within a control area should reference a specific
      generating unit.

    ControlArea: The parent control area for the generating unit specifications.
    GeneratingUnit: The generating unit specified for this control area.  Note that a control area should include a
      GeneratingUnit only once.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ControlAreaGeneratingUnit(*args, **kwargs)

    ControlArea: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    GeneratingUnit: Optional[str] = Field(
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
# "import ControlAreaGeneratingUnit"
# work as well as
# "from ControlAreaGeneratingUnit import ControlAreaGeneratingUnit".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ControlAreaGeneratingUnit
