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
class WindContPType4bIEC(IdentifiedObject, ModuleType):
    """
    P control model type 4B. Reference: IEC 61400-27-1:2015, 5.6.5.6.

    dpmaxp4b: Maximum wind turbine power ramp rate (dpmaxp4B). It is a project-dependent parameter.
    tpaero: Time constant in aerodynamic power response (Tpaero) (>= 0). It is a type-dependent parameter.
    tpordp4b: Time constant in power order lag (Tpordp4B) (>= 0). It is a type-dependent parameter.
    tufiltp4b: Voltage measurement filter time constant (Tufiltp4B) (>= 0). It is a type-dependent parameter.
    WindTurbineType4bIEC: Wind turbine type 4B model with which this wind control P type 4B model is associated.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return WindContPType4bIEC(*args, **kwargs)

    dpmaxp4b: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tpaero: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tpordp4b: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tufiltp4b: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType4bIEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

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
# "import WindContPType4bIEC"
# work as well as
# "from WindContPType4bIEC import WindContPType4bIEC".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = WindContPType4bIEC
