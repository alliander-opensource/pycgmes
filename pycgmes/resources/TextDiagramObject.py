"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DiagramObject import DiagramObject


@dataclass(config=DataclassConfig)
class TextDiagramObject(DiagramObject):
    """
    A diagram object for placing free-text or text derived from an associated domain object.

    text: The text that is displayed by this text diagram object.
    """

    text: str = Field(
        default="",
        in_profiles=[
            Profile.DL,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DL,
        }
