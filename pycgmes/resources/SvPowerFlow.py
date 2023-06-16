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
class SvPowerFlow(Base):
    """
    State variable for power flow. Load convention is used for flow direction. This means flow out from the
      TopologicalNode into the equipment is positive.

    p: The active power flow. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode
      (bus) into the conducting equipment.
    q: The reactive power flow. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode
      (bus) into the conducting equipment.
    Terminal: The terminal associated with the power flow state variable.
    """

    p: float = 0.0  # Type #ActivePower in CIM
    q: float = 0.0  # Type #ReactivePower in CIM
    Terminal: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=SvPowerFlow"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "p": [
                Profile.SV.value,
            ],
            "q": [
                Profile.SV.value,
            ],
            "Terminal": [
                Profile.SV.value,
            ],
        }
