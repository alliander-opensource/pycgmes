"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class SvTapStep(Base):
    """
    State variable for transformer tap step.

    position: The floating point tap position.   This is not the tap ratio, but rather the tap step position as defined
      by the related tap changer model and normally is constrained to be within the range of minimum and
      maximum tap positions.
    TapChanger: The tap changer associated with the tap step state.
    """

    position: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SV,
        ],
    )

    TapChanger: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SV,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.SV,
        }
