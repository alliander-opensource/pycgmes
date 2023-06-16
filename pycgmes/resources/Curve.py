"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class Curve(IdentifiedObject):
    """
    A multi-purpose curve or functional relationship between an independent variable (X-axis) and dependent (Y-axis)
      variables.

    curveStyle: The style or shape of the curve.
    xUnit: The X-axis units of measure.
    y1Unit: The Y1-axis units of measure.
    y2Unit: The Y2-axis units of measure.
    CurveDatas: The point data values that define this curve.
    """

    curveStyle: Optional[str] = None  # Type M:1..1 in CIM
    xUnit: Optional[str] = None  # Type M:1..1 in CIM
    y1Unit: Optional[str] = None  # Type M:1..1 in CIM
    y2Unit: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # CurveDatas : list = field(default_factory=list)  # Type M:1..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=Curve"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "curveStyle": [
                Profile.EQ.value,
            ],
            "xUnit": [
                Profile.EQ.value,
            ],
            "y1Unit": [
                Profile.EQ.value,
            ],
            "y2Unit": [
                Profile.EQ.value,
            ],
            "CurveDatas": [
                Profile.EQ.value,
            ],
        }
