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
class TieFlow(IdentifiedObject):
    """
    Defines the structure (in terms of location and direction) of the net interchange constraint for a control area.
      This constraint may be used by either AGC or power flow.

    ControlArea: The control area of the tie flows.
    Terminal: The terminal to which this tie flow belongs.
    positiveFlowIn: Specifies the sign of the tie flow associated with a control area. True if positive flow into the
      terminal (load convention) is also positive flow into the control area.  See the description
      of ControlArea for further explanation of how TieFlow.positiveFlowIn is used.
    """

    ControlArea: Optional[str] = None  # Type M:1 in CIM
    Terminal: Optional[str] = None  # Type M:1 in CIM
    positiveFlowIn: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=TieFlow"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "Terminal": [
                Profile.EQ.value,
            ],
            "positiveFlowIn": [
                Profile.EQ.value,
            ],
        }
