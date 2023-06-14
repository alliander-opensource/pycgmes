"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class PhaseTapChangerTable(IdentifiedObject):
    """
    Describes a tabular curve for how the phase angle difference and impedance varies with the tap step.

    PhaseTapChangerTablePoint: The points of this table.
    PhaseTapChangerTabular: The phase tap changers to which this phase tap table applies.
    """

    # *Association not used*
    # PhaseTapChangerTablePoint : list = field(default_factory=list)  # Type M:1..n in CIM
    # *Association not used*
    # PhaseTapChangerTabular : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PhaseTapChangerTable"]
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
            "PhaseTapChangerTablePoint": [
                Profile.EQ.value,
            ],
            "PhaseTapChangerTabular": [
                Profile.EQ.value,
            ],
        }
