"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .Limit import Limit


@dataclass(config=DataclassConfig)
class AnalogLimit(Limit):
    """
    Limit values for Analog measurements.

    value: The value to supervise against.
    LimitSet: The set of limits.
    """

    value: float = Field(
        default=0.0,
        in_profiles=[
            Profile.OP,
        ],
    )

    LimitSet: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
