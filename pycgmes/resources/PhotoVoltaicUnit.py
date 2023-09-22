"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .PowerElectronicsUnit import PowerElectronicsUnit


@dataclass(config=DataclassConfig)
class PhotoVoltaicUnit(PowerElectronicsUnit, ModuleType):
    """
    A photovoltaic device or an aggregation of such devices.

    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return PhotoVoltaicUnit(*args, **kwargs)

    # No attributes defined for this class.

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
# "import PhotoVoltaicUnit"
# work as well as
# "from PhotoVoltaicUnit import PhotoVoltaicUnit".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = PhotoVoltaicUnit
