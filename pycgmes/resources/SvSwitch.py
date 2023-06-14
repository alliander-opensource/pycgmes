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
class SvSwitch(Base):
    """
    State variable for switch.

    open: The attribute tells if the computed state of the switch is considered open.
    Switch: The switch associated with the switch state.
    """

    open: bool = False  # Type #Boolean in CIM
    Switch: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=SvSwitch"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.SV.value,
            ],
            # Attributes
            "open": [
                Profile.SV.value,
            ],
            "Switch": [
                Profile.SV.value,
            ],
        }
