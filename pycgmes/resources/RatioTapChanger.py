"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
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

    stepVoltageIncrement: float = 0.0  # Type #PerCent in CIM
    RatioTapChangerTable: Optional[str] = None  # Type M:0..1 in CIM
    TransformerEnd: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=RatioTapChanger"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.EQ.value,
                Profile.SSH.value,
            ],
            # Attributes
            "stepVoltageIncrement": [
                Profile.EQ.value,
            ],
            "RatioTapChangerTable": [
                Profile.EQ.value,
            ],
            "TransformerEnd": [
                Profile.EQ.value,
            ],
        }
