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
class WindGenType3IEC(IdentifiedObject, ModuleType):
    """
    Parent class supporting relationships to IEC wind turbines type 3 generator models of IEC type 3A and 3B.

    dipmax: Maximum active current ramp rate (dipmax). It is a project-dependent parameter.
    diqmax: Maximum reactive current ramp rate (diqmax). It is a project-dependent parameter.
    xs: Electromagnetic transient reactance (xS). It is a type-dependent parameter.
    WindTurbineType3IEC: Wind turbine type 3 model with which this wind generator type 3 is associated.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return WindGenType3IEC(*args, **kwargs)

    dipmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    diqmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    xs: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
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
# "import WindGenType3IEC"
# work as well as
# "from WindGenType3IEC import WindGenType3IEC".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = WindGenType3IEC
