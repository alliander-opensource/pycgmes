"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindAeroOneDimIEC(IdentifiedObject, ModuleType):
    """
    One-dimensional aerodynamic model.   Reference: IEC 61400-27-1:2015, 5.6.1.2.

    ka: Aerodynamic gain (ka). It is a type-dependent parameter.
    thetaomega: Initial pitch angle (thetaomega0). It is a case-dependent parameter.
    WindTurbineType3IEC: Wind turbine type 3 model with which this wind aerodynamic model is associated.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return WindAeroOneDimIEC(*args, **kwargs)

    ka: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    thetaomega: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType3IEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

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
# "import WindAeroOneDimIEC"
# work as well as
# "from WindAeroOneDimIEC import WindAeroOneDimIEC".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = WindAeroOneDimIEC
