"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Base import Base


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    pInjection: float = 0.0  # Type #ActivePower in CIM
    qInjection: float = 0.0  # Type #ReactivePower in CIM
    TopologicalNode: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=SvInjection\n"
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
                self.profiles.SV.value,
            ],
            # Attributes
            "pInjection": [
                self.profiles.SV.value,
            ],
            "qInjection": [
                self.profiles.SV.value,
            ],
            "TopologicalNode": [
                self.profiles.SV.value,
            ],
        }
