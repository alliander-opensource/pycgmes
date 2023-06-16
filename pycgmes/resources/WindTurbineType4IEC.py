"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .WindTurbineType3or4IEC import WindTurbineType3or4IEC


@dataclass(config=DataclassConfig)
class WindTurbineType4IEC(WindTurbineType3or4IEC):
    """
    Parent class supporting relationships to IEC wind turbines type 4 including their control models.

    WindGenType3aIEC: Wind generator type 3A model associated with this wind turbine type 4 model.
    """

    WindGenType3aIEC: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindTurbineType4IEC"]
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
                Profile.DY.value,
            ],
            # Attributes
            "WindGenType3aIEC": [
                Profile.DY.value,
            ],
        }
