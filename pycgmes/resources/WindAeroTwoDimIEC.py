"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindAeroTwoDimIEC(IdentifiedObject):
    """
    Two-dimensional aerodynamic model.   Reference: IEC 61400-27-1:2015, 5.6.1.3.

    dpomega: Partial derivative of aerodynamic power with respect to changes in WTR speed (dpomega). It is a type-
      dependent parameter.
    dptheta: Partial derivative of aerodynamic power with respect to changes in pitch angle (dptheta). It is a type-
      dependent parameter.
    dpv1: Partial derivative (dpv1). It is a type-dependent parameter.
    omegazero: Rotor speed if the wind turbine is not derated (omega0). It is a type-dependent parameter.
    pavail: Available aerodynamic power (pavail). It is a case-dependent parameter.
    thetazero: Pitch angle if the wind turbine is not derated (theta0). It is a case-dependent parameter.
    thetav2: Blade angle at twice rated wind speed (thetav2). It is a type-dependent parameter.
    WindTurbineType3IEC: Wind turbine type 3 model with which this wind aerodynamic model is associated.
    """

    dpomega: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dptheta: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dpv1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    omegazero: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pavail: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    thetazero: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    thetav2: float = Field(
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
