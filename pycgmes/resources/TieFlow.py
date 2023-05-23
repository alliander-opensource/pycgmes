"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ControlArea: Optional[str] = None  # Type M:1 in CIM
    Terminal: Optional[str] = None  # Type M:1 in CIM
    positiveFlowIn: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=TieFlow\n"
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
            "Terminal": [
                self.profiles.EQ.value,
            ],
            "positiveFlowIn": [
                self.profiles.EQ.value,
            ],
        }
