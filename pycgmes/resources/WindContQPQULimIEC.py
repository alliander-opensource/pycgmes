"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindContQPQULimIEC(IdentifiedObject):
    """
    QP and QU limitation model. Reference: IEC 61400-27-1:2015, 5.6.5.10.

    tpfiltql: Power measurement filter time constant for Q capacity (Tpfiltql) (>= 0). It is a type-dependent parameter.
    tufiltql: Voltage measurement filter time constant for Q capacity (Tufiltql) (>= 0). It is a type-dependent
      parameter.
    WindTurbineType3or4IEC: Wind generator type 3 or type 4 model with which this QP and QU limitation model is
      associated.
    WindDynamicsLookupTable: The wind dynamics lookup table associated with this QP and QU limitation model.
    """

    tpfiltql: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tufiltql: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType3or4IEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # WindDynamicsLookupTable : list = Field(default_factory=list, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
