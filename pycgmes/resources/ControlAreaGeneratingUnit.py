"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class ControlAreaGeneratingUnit(IdentifiedObject):
    """
    A control area generating unit. This class is needed so that alternate control area definitions may include the same
      generating unit.   It should be noted that only one instance within a control area should reference a specific
      generating unit.

    ControlArea: The parent control area for the generating unit specifications.
    GeneratingUnit: The generating unit specified for this control area.  Note that a control area should include a
      GeneratingUnit only once.
    """

    ControlArea: Optional[str] = None  # Type M:1 in CIM
    GeneratingUnit: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ControlAreaGeneratingUnit"]
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
            "ControlArea": [
                Profile.EQ.value,
            ],
            "GeneratingUnit": [
                Profile.EQ.value,
            ],
        }
