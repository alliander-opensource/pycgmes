"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .PowerSystemResource import PowerSystemResource


@dataclass(config=DataclassConfig)
class CAESPlant(PowerSystemResource, ModuleType):
    """
    Compressed air energy storage plant.

    ThermalGeneratingUnit: A thermal generating unit may be a member of a compressed air energy storage plant.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return CAESPlant(*args, **kwargs)

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # ThermalGeneratingUnit : Optional[str] = Field(default=None, in_profiles = [Profile.EQ, ])

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
# "import CAESPlant"
# work as well as
# "from CAESPlant import CAESPlant".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = CAESPlant
