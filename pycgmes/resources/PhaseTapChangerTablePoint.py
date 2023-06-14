"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TapChangerTablePoint import TapChangerTablePoint


@dataclass(config=DataclassConfig)
class PhaseTapChangerTablePoint(TapChangerTablePoint):
    """
    Describes each tap step in the phase tap changer tabular curve.

    PhaseTapChangerTable: The table of this point.
    angle: The angle difference in degrees. A positive value indicates a positive angle variation from the Terminal at
      the  PowerTransformerEnd,  where the TapChanger is located, into the transformer.
    """

    PhaseTapChangerTable: Optional[str] = None  # Type M:1 in CIM
    angle: float = 0.0  # Type #AngleDegrees in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PhaseTapChangerTablePoint"]
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
            ],
            # Attributes
            "PhaseTapChangerTable": [
                Profile.EQ.value,
            ],
            "angle": [
                Profile.EQ.value,
            ],
        }
