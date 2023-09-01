"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindMechIEC(IdentifiedObject):
    """
    Two mass model. Reference: IEC 61400-27-1:2015, 5.6.2.1.

    cdrt: Drive train damping (cdrt). It is a type-dependent parameter.
    hgen: Inertia constant of generator (Hgen) (>= 0). It is a type-dependent parameter.
    hwtr: Inertia constant of wind turbine rotor (HWTR) (>= 0). It is a type-dependent parameter.
    kdrt: Drive train stiffness (kdrt). It is a type-dependent parameter.
    WindTurbineType3IEC: Wind turbine type 3 model with which this wind mechanical model is associated.
    WindTurbineType1or2IEC: Wind generator type 1 or type 2 model with which this wind mechanical model is associated.
    WindTurbineType4bIEC: Wind turbine type 4B model with which this wind mechanical model is associated.
    """

    cdrt: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    hgen: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    hwtr: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kdrt: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType3IEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType1or2IEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

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
