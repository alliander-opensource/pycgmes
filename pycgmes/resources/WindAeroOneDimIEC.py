"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindAeroOneDimIEC(IdentifiedObject):
    """
    One-dimensional aerodynamic model.   Reference: IEC 61400-27-1:2015, 5.6.1.2.

    ka: Aerodynamic gain (ka). It is a type-dependent parameter.
    thetaomega: Initial pitch angle (thetaomega0). It is a case-dependent parameter.
    WindTurbineType3IEC: Wind turbine type 3 model with which this wind aerodynamic model is associated.
    """

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
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
