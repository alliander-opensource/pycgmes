"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
class ControlAreaGeneratingUnit(IdentifiedObject):
    """
    A control area generating unit. This class is needed so that alternate control area definitions may include the same
      generating unit.   It should be noted that only one instance within a control area should reference a specific
      generating unit.

    ControlArea: The parent control area for the generating unit specifications.
    GeneratingUnit: The generating unit specified for this control area.  Note that a control area should include a
      GeneratingUnit only once.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ControlArea: Optional[str] = None  # Type M:1 in CIM
    GeneratingUnit: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ControlAreaGeneratingUnit\n"
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
            "ControlArea": [
                self.profiles.EQ.value,
            ],
            "GeneratingUnit": [
                self.profiles.EQ.value,
            ],
        }
