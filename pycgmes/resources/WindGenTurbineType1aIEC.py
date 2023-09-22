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

from .WindTurbineType1or2IEC import WindTurbineType1or2IEC


@dataclass(config=DataclassConfig)
class WindGenTurbineType1aIEC(WindTurbineType1or2IEC, ModuleType):
    """
    Wind turbine IEC type 1A. Reference: IEC 61400-27-1:2015, 5.5.2.2.

    WindAeroConstIEC: Wind aerodynamic model associated with this wind turbine type 1A model.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return WindGenTurbineType1aIEC(*args, **kwargs)

    WindAeroConstIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import WindGenTurbineType1aIEC"
# work as well as
# "from WindGenTurbineType1aIEC import WindGenTurbineType1aIEC".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = WindGenTurbineType1aIEC
