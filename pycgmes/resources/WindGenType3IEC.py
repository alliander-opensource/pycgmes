"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindGenType3IEC(IdentifiedObject):
    """
    Parent class supporting relationships to IEC wind turbines type 3 generator models of IEC type 3A and 3B.

    dipmax: Maximum active current ramp rate (dipmax). It is a project-dependent parameter.
    diqmax: Maximum reactive current ramp rate (diqmax). It is a project-dependent parameter.
    xs: Electromagnetic transient reactance (xS). It is a type-dependent parameter.
    WindTurbineType3IEC: Wind turbine type 3 model with which this wind generator type 3 is associated.
    """

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
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
