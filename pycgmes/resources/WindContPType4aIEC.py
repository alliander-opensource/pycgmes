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
class WindContPType4aIEC(IdentifiedObject, ModuleType):
    """
    P control model type 4A. Reference: IEC 61400-27-1:2015, 5.6.5.5.

    dpmaxp4a: Maximum wind turbine power ramp rate (dpmaxp4A). It is a project-dependent parameter.
    tpordp4a: Time constant in power order lag (Tpordp4A) (>= 0). It is a type-dependent parameter.
    tufiltp4a: Voltage measurement filter time constant (Tufiltp4A) (>= 0). It is a type-dependent parameter.
    WindTurbineType4aIEC: Wind turbine type 4A model with which this wind control P type 4A model is associated.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return WindContPType4aIEC(*args, **kwargs)

    dpmaxp4a: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tpordp4a: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tufiltp4a: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType4aIEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

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
# "import WindContPType4aIEC"
# work as well as
# "from WindContPType4aIEC import WindContPType4aIEC".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = WindContPType4aIEC
