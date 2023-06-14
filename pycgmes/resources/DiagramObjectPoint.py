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
class DiagramObjectPoint(Base):
    """
    A point in a given space defined by 3 coordinates and associated to a diagram object.  The coordinates may be
      positive or negative as the origin does not have to be in the corner of a diagram.

    DiagramObject: The diagram object with which the points are associated.
    DiagramObjectGluePoint: The `glue` point to which this point is associated.
    sequenceNumber: The sequence position of the point, used for defining the order of points for diagram objects acting
      as a polyline or polygon with more than one point. The attribute shall be a positive value.
    xPosition: The X coordinate of this point.
    yPosition: The Y coordinate of this point.
    zPosition: The Z coordinate of this point.
    """

    DiagramObject: Optional[str] = None  # Type M:1 in CIM
    DiagramObjectGluePoint: Optional[str] = None  # Type M:0..1 in CIM
    sequenceNumber: int = 0  # Type #Integer in CIM
    xPosition: float = 0.0  # Type #Float in CIM
    yPosition: float = 0.0  # Type #Float in CIM
    zPosition: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=DiagramObjectPoint"]
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
                Profile.DL.value,
            ],
            # Attributes
            "DiagramObject": [
                Profile.DL.value,
            ],
            "DiagramObjectGluePoint": [
                Profile.DL.value,
            ],
            "sequenceNumber": [
                Profile.DL.value,
            ],
            "xPosition": [
                Profile.DL.value,
            ],
            "yPosition": [
                Profile.DL.value,
            ],
            "zPosition": [
                Profile.DL.value,
            ],
        }
