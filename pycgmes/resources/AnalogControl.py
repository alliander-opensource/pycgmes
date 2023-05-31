"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Control import Control


@dataclass
class AnalogControl(Control):
    """
    An analog control used for supervisory control.

    maxValue: Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    minValue: Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    AnalogValue: The MeasurementValue that is controlled.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    maxValue: float = 0.0  # Type #Float in CIM
    minValue: float = 0.0  # Type #Float in CIM
    AnalogValue: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=AnalogControl\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.OP.value,
            ],
            # Attributes
            "maxValue": [
                self.profiles.OP.value,
            ],
            "minValue": [
                self.profiles.OP.value,
            ],
            "AnalogValue": [
                self.profiles.OP.value,
            ],
        }
