"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindContPType4aIEC(IdentifiedObject):
    """
    P control model type 4A. Reference: IEC 61400-27-1:2015, 5.6.5.5.

    dpmaxp4a: Maximum wind turbine power ramp rate (dpmaxp4A). It is a project-dependent parameter.
    tpordp4a: Time constant in power order lag (Tpordp4A) (>= 0). It is a type-dependent parameter.
    tufiltp4a: Voltage measurement filter time constant (Tufiltp4A) (>= 0). It is a type-dependent parameter.
    WindTurbineType4aIEC: Wind turbine type 4A model with which this wind control P type 4A model is associated.
    """

    dpmaxp4a: float = 0.0  # Type #PU in CIM
    tpordp4a: int = 0  # Type #Seconds in CIM
    tufiltp4a: int = 0  # Type #Seconds in CIM
    # *Association not used*
    # WindTurbineType4aIEC : Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindContPType4aIEC"]
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
            "dpmaxp4a": [
                Profile.DY.value,
            ],
            "tpordp4a": [
                Profile.DY.value,
            ],
            "tufiltp4a": [
                Profile.DY.value,
            ],
            "WindTurbineType4aIEC": [
                Profile.DY.value,
            ],
        }
