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
class WindAeroConstIEC(IdentifiedObject, ModuleType):
    """
    Constant aerodynamic torque model which assumes that the aerodynamic torque is constant. Reference: IEC
      61400-27-1:2015, 5.6.1.1.

    WindGenTurbineType1aIEC: Wind turbine type 1A model with which this wind aerodynamic model is associated.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return WindAeroConstIEC(*args, **kwargs)

    # *Association not used*
    # Type M:1 in CIM  # pylint: disable-next=line-too-long
    # WindGenTurbineType1aIEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

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
# "import WindAeroConstIEC"
# work as well as
# "from WindAeroConstIEC import WindAeroConstIEC".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = WindAeroConstIEC
