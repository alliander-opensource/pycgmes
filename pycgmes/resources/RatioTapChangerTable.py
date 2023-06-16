"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class RatioTapChangerTable(IdentifiedObject):
    """
    Describes a curve for how the voltage magnitude and impedance varies with the tap step.

    RatioTapChanger: The ratio tap changer of this tap ratio table.
    RatioTapChangerTablePoint: Points of this table.
    """

    # *Association not used*
    # RatioTapChanger : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # RatioTapChangerTablePoint : list = field(default_factory=list)  # Type M:1..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=RatioTapChangerTable"]
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
            ],
            # Attributes
            "RatioTapChanger": [
                Profile.EQ.value,
            ],
            "RatioTapChangerTablePoint": [
                Profile.EQ.value,
            ],
        }
