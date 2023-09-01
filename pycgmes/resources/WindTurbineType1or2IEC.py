"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .WindTurbineType1or2Dynamics import WindTurbineType1or2Dynamics


@dataclass(config=DataclassConfig)
class WindTurbineType1or2IEC(WindTurbineType1or2Dynamics):
    """
    Parent class supporting relationships to IEC wind turbines type 1 and type 2 including their control models.
      Generator model for wind turbine of IEC type 1 or type 2 is a standard asynchronous generator model.
      Reference: IEC 61400-27-1:2015, 5.5.2 and 5.5.3.

    WindMechIEC: Wind mechanical model associated with this wind generator type 1 or type 2 model.
    WindProtectionIEC: Wind turbune protection model associated with this wind generator type 1 or type 2 model.
    """

    WindMechIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindProtectionIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
