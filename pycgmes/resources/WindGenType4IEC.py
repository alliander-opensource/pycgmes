"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindGenType4IEC(IdentifiedObject):
    """
    IEC type 4 generator set model. Reference: IEC 61400-27-1:2015, 5.6.3.4.

    dipmax: Maximum active current ramp rate (dipmax). It is a project-dependent parameter.
    diqmin: Minimum reactive current ramp rate (diqmin). It is a project-dependent parameter.
    diqmax: Maximum reactive current ramp rate (diqmax). It is a project-dependent parameter.
    tg: Time constant (Tg) (>= 0). It is a type-dependent parameter.
    WindTurbineType4aIEC: Wind turbine type 4A model with which this wind generator type 4 model is associated.
    WindTurbineType4bIEC: Wind turbine type 4B model with which this wind generator type 4 model is associated.
    """

    dipmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    diqmin: float = Field(
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

    tg: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType4aIEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType4bIEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
