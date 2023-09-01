"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .WindGenType3IEC import WindGenType3IEC


@dataclass(config=DataclassConfig)
class WindGenType3aIEC(WindGenType3IEC):
    """
    IEC type 3A generator set model. Reference: IEC 61400-27-1:2015, 5.6.3.2.

    kpc: Current PI controller proportional gain (KPc). It is a type-dependent parameter.
    tic: Current PI controller integration time constant (TIc) (>= 0). It is a type-dependent parameter.
    WindTurbineType4IEC: Wind turbine type 4 model with which this wind generator type 3A model is associated.
    """

    kpc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tic: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType4IEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
