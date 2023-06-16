"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .WindTurbineType1or2IEC import WindTurbineType1or2IEC


@dataclass(config=DataclassConfig)
class WindGenTurbineType1aIEC(WindTurbineType1or2IEC):
    """
    Wind turbine IEC type 1A. Reference: IEC 61400-27-1:2015, 5.5.2.2.

    WindAeroConstIEC: Wind aerodynamic model associated with this wind turbine type 1A model.
    """

    WindAeroConstIEC: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindGenTurbineType1aIEC"]
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
            "WindAeroConstIEC": [
                Profile.DY.value,
            ],
        }
