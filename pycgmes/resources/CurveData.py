"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Base import Base


@dataclass
class CurveData(Base):
    """
    Multi-purpose data points for defining a curve.  The use of this generic class is discouraged if a more specific
      class can be used to specify the X and Y axis values along with their specific data types.

    Curve: The curve of  this curve data point.
    xvalue: The data value of the X-axis variable,  depending on the X-axis units.
    y1value: The data value of the  first Y-axis variable, depending on the Y-axis units.
    y2value: The data value of the second Y-axis variable (if present), depending on the Y-axis units.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    Curve: Optional[str] = None  # Type M:1 in CIM
    xvalue: float = 0.0  # Type #Float in CIM
    y1value: float = 0.0  # Type #Float in CIM
    y2value: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=CurveData\n"
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
                self.profiles.EQ.value,
            ],
            # Attributes
            "Curve": [
                self.profiles.EQ.value,
            ],
            "xvalue": [
                self.profiles.EQ.value,
            ],
            "y1value": [
                self.profiles.EQ.value,
            ],
            "y2value": [
                self.profiles.EQ.value,
            ],
        }
