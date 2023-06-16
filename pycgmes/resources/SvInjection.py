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
class SvInjection(Base):
    """
    The SvInjection reports the calculated bus injection minus the sum of the terminal flows. The terminal flow is
      positive out from the bus (load sign convention) and bus injection has positive flow into the bus. SvInjection
      may have the remainder after state estimation or slack after power flow calculation.

    pInjection: The active power mismatch between calculated injection and initial injection.  Positive sign means
      injection into the TopologicalNode (bus).
    qInjection: The reactive power mismatch between calculated injection and initial injection.  Positive sign means
      injection into the TopologicalNode (bus).
    TopologicalNode: The topological node associated with the flow injection state variable.
    """

    pInjection: float = 0.0  # Type #ActivePower in CIM
    qInjection: float = 0.0  # Type #ReactivePower in CIM
    TopologicalNode: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=SvInjection"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "pInjection": [
                Profile.SV.value,
            ],
            "qInjection": [
                Profile.SV.value,
            ],
            "TopologicalNode": [
                Profile.SV.value,
            ],
        }
