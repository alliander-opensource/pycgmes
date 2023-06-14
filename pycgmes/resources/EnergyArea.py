"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class EnergyArea(IdentifiedObject):
    """
    Describes an area having energy production or consumption.  Specializations are intended to support the load
      allocation function as typically required in energy management systems or planning studies to allocate
      hypothesized load levels to individual load points for power flow analysis.  Often the energy area can be
      linked to both measured and forecast load levels.

    ControlArea: The control area specification that is used for the load forecast.
    """

    # *Association not used*
    # ControlArea : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=EnergyArea"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
        }
