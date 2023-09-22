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
class HydroPump(Equipment, ModuleType):
    """
    A synchronous motor-driven pump, typically associated with a pumped storage plant.

    HydroPowerPlant: The hydro pump may be a member of a pumped storage plant or a pump for distributing water.
    RotatingMachine: The synchronous machine drives the turbine which moves the water from a low elevation to a higher
      elevation. The direction of machine rotation for pumping may or may not be the same as for
      generating.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return HydroPump(*args, **kwargs)

    HydroPowerPlant: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    RotatingMachine: Optional[str] = Field(
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
# "import HydroPump"
# work as well as
# "from HydroPump import HydroPump".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = HydroPump
