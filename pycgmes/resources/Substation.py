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
class Substation(EquipmentContainer):
    """
    A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk
      is passed for the purposes of switching or modifying its characteristics.

    Region: The SubGeographicalRegion containing the substation.
    VoltageLevels: The voltage levels within this substation.
    DCConverterUnit: The DC converter unit belonging of the substation.
    """

    Region: Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # VoltageLevels : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # DCConverterUnit : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=Substation"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "Region": [
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            "VoltageLevels": [
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            "DCConverterUnit": [
                Profile.EQ.value,
            ],
        }
