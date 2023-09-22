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

from .WindGenType3IEC import WindGenType3IEC


@dataclass(config=DataclassConfig)
class WindGenType3bIEC(WindGenType3IEC, ModuleType):
    """
    IEC type 3B generator set model. Reference: IEC 61400-27-1:2015, 5.6.3.3.

    WindDynamicsLookupTable: The wind dynamics lookup table associated with this generator type 3B model.
    mwtcwp: Crowbar control mode (MWTcwp). It is a case-dependent parameter. true = 1 in the IEC model false = 0 in the
      IEC model.
    tg: Current generation time constant (Tg) (>= 0). It is a type-dependent parameter.
    two: Time constant for crowbar washout filter (Two) (>= 0). It is a case-dependent parameter.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return WindGenType3bIEC(*args, **kwargs)

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # WindDynamicsLookupTable : list = Field(default_factory=list, in_profiles = [Profile.DY, ])

    mwtcwp: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    tg: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    two: int = Field(
        default=0,
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
# "import WindGenType3bIEC"
# work as well as
# "from WindGenType3bIEC import WindGenType3bIEC".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = WindGenType3bIEC
