"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    curveStyle: Optional[str] = None  # Type M:1..1 in CIM
    xUnit: Optional[str] = None  # Type M:1..1 in CIM
    y1Unit: Optional[str] = None  # Type M:1..1 in CIM
    y2Unit: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # CurveDatas : list = field(default_factory=list)  # Type M:1..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=Curve\n"
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
            "curveStyle": [
                self.profiles.EQ.value,
            ],
            "xUnit": [
                self.profiles.EQ.value,
            ],
            "y1Unit": [
                self.profiles.EQ.value,
            ],
            "y2Unit": [
                self.profiles.EQ.value,
            ],
            "CurveDatas": [
                self.profiles.EQ.value,
            ],
        }
