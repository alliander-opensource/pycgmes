"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class RatioTapChangerTable(IdentifiedObject, ModuleType):
    """
    Describes a curve for how the voltage magnitude and impedance varies with the tap step.

    RatioTapChanger: The ratio tap changer of this tap ratio table.
    RatioTapChangerTablePoint: Points of this table.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return RatioTapChangerTable(*args, **kwargs)

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # RatioTapChanger : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # RatioTapChangerTablePoint : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

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
# "import RatioTapChangerTable"
# work as well as
# "from RatioTapChangerTable import RatioTapChangerTable".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = RatioTapChangerTable
