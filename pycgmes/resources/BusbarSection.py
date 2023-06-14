"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Connector import Connector


@dataclass(config=DataclassConfig)
class BusbarSection(Connector):
    """
    A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment
      within a single substation.  Voltage measurements are typically obtained from voltage transformers that are
      connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled
      with exactly one logical terminal.

    ipMax: Maximum allowable peak short-circuit current of busbar (Ipmax in IEC 60909-0).  Mechanical limit of the
      busbar in the substation itself. Used for short circuit data exchange according to IEC 60909.
    """

    ipMax: float = 0.0  # Type #CurrentFlow in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=BusbarSection"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.SC.value,
            ],
            # Attributes
            "ipMax": [
                Profile.SC.value,
            ],
        }
