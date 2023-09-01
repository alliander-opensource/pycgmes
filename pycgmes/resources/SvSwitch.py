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
class SvSwitch(Base):
    """
    State variable for switch.

    open: The attribute tells if the computed state of the switch is considered open.
    Switch: The switch associated with the switch state.
    """

    open: bool = Field(
        default=False,
        in_profiles=[
            Profile.SV,
        ],
    )

    Switch: Optional[str] = Field(
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
