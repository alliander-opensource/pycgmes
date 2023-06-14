"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PhaseTapChanger import PhaseTapChanger


@dataclass(config=DataclassConfig)
class PhaseTapChangerTabular(PhaseTapChanger):
    """
    Describes a tap changer with a table defining the relation between the tap step and the phase angle difference
      across the transformer.

    PhaseTapChangerTable: The phase tap changer table for this phase tap changer.
    """

    PhaseTapChangerTable: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PhaseTapChangerTabular"]
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
            "PhaseTapChangerTable": [
                Profile.EQ.value,
            ],
        }
