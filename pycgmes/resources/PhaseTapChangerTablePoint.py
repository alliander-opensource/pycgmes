"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .TapChangerTablePoint import TapChangerTablePoint


@dataclass
class PhaseTapChangerTablePoint(TapChangerTablePoint):
    """
    Describes each tap step in the phase tap changer tabular curve.

    PhaseTapChangerTable: The table of this point.
    angle: The angle difference in degrees. A positive value indicates a positive angle variation from the Terminal at
      the  PowerTransformerEnd,  where the TapChanger is located, into the transformer.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    PhaseTapChangerTable: Optional[str] = None  # Type M:1 in CIM
    angle: float = 0.0  # Type #AngleDegrees in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PhaseTapChangerTablePoint\n"
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
            "PhaseTapChangerTable": [
                self.profiles.EQ.value,
            ],
            "angle": [
                self.profiles.EQ.value,
            ],
        }
