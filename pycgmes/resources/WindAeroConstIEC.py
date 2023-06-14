"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindAeroConstIEC(IdentifiedObject):
    """
    Constant aerodynamic torque model which assumes that the aerodynamic torque is constant. Reference: IEC
      61400-27-1:2015, 5.6.1.1.

    WindGenTurbineType1aIEC: Wind turbine type 1A model with which this wind aerodynamic model is associated.
    """

    # *Association not used*
    # WindGenTurbineType1aIEC : Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindAeroConstIEC"]
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
            "WindGenTurbineType1aIEC": [
                Profile.DY.value,
            ],
        }
