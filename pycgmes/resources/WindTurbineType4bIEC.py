"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .WindTurbineType4IEC import WindTurbineType4IEC


@dataclass(config=DataclassConfig)
class WindTurbineType4bIEC(WindTurbineType4IEC):
    """
    Wind turbine IEC type 4B. Reference: IEC 61400-27-1:2015, 5.5.5.3.

    WindContPType4bIEC: Wind control P type 4B model associated with this wind turbine type 4B model.
    WindGenType4IEC: Wind generator type 4 model associated with this wind turbine type 4B model.
    WindMechIEC: Wind mechanical model associated with this wind turbine type 4B model.
    """

    WindContPType4bIEC: Optional[str] = None  # Type M:1 in CIM
    WindGenType4IEC: Optional[str] = None  # Type M:0..1 in CIM
    WindMechIEC: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindTurbineType4bIEC"]
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
            "WindContPType4bIEC": [
                Profile.DY.value,
            ],
            "WindGenType4IEC": [
                Profile.DY.value,
            ],
            "WindMechIEC": [
                Profile.DY.value,
            ],
        }
