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

from .EnergyConnection import EnergyConnection


@dataclass(config=DataclassConfig)
class RegulatingCondEq(EnergyConnection, ModuleType):
    """
    A type of conducting equipment that can regulate a quantity (i.e. voltage or flow) at a specific point in the
      network.

    RegulatingControl: The regulating control scheme in which this equipment participates.
    controlEnabled: Specifies the regulation status of the equipment.  True is regulating, false is not regulating.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return RegulatingCondEq(*args, **kwargs)

    RegulatingControl: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    controlEnabled: bool = Field(
        default=False,
        in_profiles=[
            Profile.SSH,
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
            Profile.SC,
            Profile.SSH,
            Profile.DY,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import RegulatingCondEq"
# work as well as
# "from RegulatingCondEq import RegulatingCondEq".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = RegulatingCondEq
