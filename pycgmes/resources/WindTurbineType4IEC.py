"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .WindTurbineType3or4IEC import WindTurbineType3or4IEC


@dataclass(config=DataclassConfig)
class WindTurbineType4IEC(WindTurbineType3or4IEC):
    """
    Parent class supporting relationships to IEC wind turbines type 4 including their control models.

    WindGenType3aIEC: Wind generator type 3A model associated with this wind turbine type 4 model.
    """

    WindGenType3aIEC: Optional[str] = Field(
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
