"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindRefFrameRotIEC(IdentifiedObject):
    """
    Reference frame rotation model. Reference: IEC 61400-27-1:2015, 5.6.3.5.

    tpll: Time constant for PLL first order filter model (TPLL) (>= 0). It is a type-dependent parameter.
    upll1: Voltage below which the angle of the voltage is filtered and possibly also frozen (uPLL1). It is a type-
      dependent parameter.
    upll2: Voltage (uPLL2) below which the angle of the voltage is frozen if uPLL2 is smaller or equal to uPLL1 . It is
      a type-dependent parameter.
    WindTurbineType3or4IEC: Wind turbine type 3 or type 4 model with which this reference frame rotation model is
      associated.
    """

    tpll: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    upll1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    upll2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType3or4IEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
