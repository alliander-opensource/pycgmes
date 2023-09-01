"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TapChanger import TapChanger


@dataclass(config=DataclassConfig)
class RatioTapChanger(TapChanger):
    """
    A tap changer that changes the voltage ratio impacting the voltage magnitude but not the phase angle across the
      transformer.  Angle sign convention (general): Positive value indicates a positive phase shift from the
      winding where the tap is located to the other winding (for a two-winding transformer).

    stepVoltageIncrement: Tap step increment, in per cent of rated voltage of the power transformer end, per step
      position. When the increment is negative, the voltage decreases when the tap step
      increases.
    RatioTapChangerTable: The tap ratio table for this ratio  tap changer.
    TransformerEnd: Transformer end to which this ratio tap changer belongs.
    """

    stepVoltageIncrement: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    RatioTapChangerTable: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    TransformerEnd: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SSH,
        }
