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

from .TapChangerTablePoint import TapChangerTablePoint


@dataclass(config=DataclassConfig)
class PhaseTapChangerTablePoint(TapChangerTablePoint, ModuleType):
    """
    Describes each tap step in the phase tap changer tabular curve.

    PhaseTapChangerTable: The table of this point.
    angle: The angle difference in degrees. A positive value indicates a positive angle variation from the Terminal at
      the  PowerTransformerEnd,  where the TapChanger is located, into the transformer.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return PhaseTapChangerTablePoint(*args, **kwargs)

    PhaseTapChangerTable: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    angle: float = Field(
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
# "import PhaseTapChangerTablePoint"
# work as well as
# "from PhaseTapChangerTablePoint import PhaseTapChangerTablePoint".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = PhaseTapChangerTablePoint
