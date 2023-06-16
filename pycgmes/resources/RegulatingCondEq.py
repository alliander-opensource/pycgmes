"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .EnergyConnection import EnergyConnection


@dataclass(config=DataclassConfig)
class RegulatingCondEq(EnergyConnection):
    """
    A type of conducting equipment that can regulate a quantity (i.e. voltage or flow) at a specific point in the
      network.

    RegulatingControl: The regulating control scheme in which this equipment participates.
    controlEnabled: Specifies the regulation status of the equipment.  True is regulating, false is not regulating.
    """

    RegulatingControl: Optional[str] = None  # Type M:0..1 in CIM
    controlEnabled: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=RegulatingCondEq"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.SSH.value,
                Profile.DY.value,
            ],
            # Attributes
            "RegulatingControl": [
                Profile.EQ.value,
            ],
            "controlEnabled": [
                Profile.SSH.value,
            ],
        }
