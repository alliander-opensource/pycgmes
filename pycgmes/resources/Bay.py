"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .EquipmentContainer import EquipmentContainer


@dataclass(config=DataclassConfig)
class Bay(EquipmentContainer):
    """
    A collection of power system resources (within a given substation) including conducting equipment, protection
      relays, measurements, and telemetry.  A bay typically represents a physical grouping related to modularization
      of equipment.

    VoltageLevel: The voltage level containing this bay.
    """

    VoltageLevel: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=Bay"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            # Attributes
            "VoltageLevel": [
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
        }
