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

from .WindTurbineType3or4IEC import WindTurbineType3or4IEC


@dataclass(config=DataclassConfig)
class WindTurbineType4IEC(WindTurbineType3or4IEC, ModuleType):
    """
    Parent class supporting relationships to IEC wind turbines type 4 including their control models.

    WindGenType3aIEC: Wind generator type 3A model associated with this wind turbine type 4 model.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return WindTurbineType4IEC(*args, **kwargs)

    WindGenType3aIEC: Optional[str] = Field(
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
# "import WindTurbineType4IEC"
# work as well as
# "from WindTurbineType4IEC import WindTurbineType4IEC".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = WindTurbineType4IEC
