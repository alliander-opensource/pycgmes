"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DiagramObject import DiagramObject


@dataclass(config=DataclassConfig)
class TextDiagramObject(DiagramObject):
    """
    A diagram object for placing free-text or text derived from an associated domain object.

    text: The text that is displayed by this text diagram object.
    """

    text: str = ""  # Type #String in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=TextDiagramObject"]
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
            "text": [
                Profile.DL.value,
            ],
        }
