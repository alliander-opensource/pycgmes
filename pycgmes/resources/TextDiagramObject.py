"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .DiagramObject import DiagramObject


@dataclass
class TextDiagramObject(DiagramObject):
    """
    A diagram object for placing free-text or text derived from an associated domain object.

    text: The text that is displayed by this text diagram object.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    text: str = ""  # Type #String in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=TextDiagramObject\n"
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
                self.profiles.DL.value,
            ],
            # Attributes
            "text": [
                self.profiles.DL.value,
            ],
        }
