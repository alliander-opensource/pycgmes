"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class CurveData(Base):
    """
    Multi-purpose data points for defining a curve.  The use of this generic class is discouraged if a more specific
      class can be used to specify the X and Y axis values along with their specific data types.

    Curve: The curve of  this curve data point.
    xvalue: The data value of the X-axis variable,  depending on the X-axis units.
    y1value: The data value of the  first Y-axis variable, depending on the Y-axis units.
    y2value: The data value of the second Y-axis variable (if present), depending on the Y-axis units.
    """

    Curve: Optional[str] = None  # Type M:1 in CIM
    xvalue: float = 0.0  # Type #Float in CIM
    y1value: float = 0.0  # Type #Float in CIM
    y2value: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=CurveData"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            ],
            # Attributes
            "Curve": [
                Profile.EQ.value,
            ],
            "xvalue": [
                Profile.EQ.value,
            ],
            "y1value": [
                Profile.EQ.value,
            ],
            "y2value": [
                Profile.EQ.value,
            ],
        }
