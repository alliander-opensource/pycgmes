"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindGenType4IEC(IdentifiedObject):
    """
    IEC type 4 generator set model. Reference: IEC 61400-27-1:2015, 5.6.3.4.

    dipmax: Maximum active current ramp rate (dipmax). It is a project-dependent parameter.
    diqmin: Minimum reactive current ramp rate (diqmin). It is a project-dependent parameter.
    diqmax: Maximum reactive current ramp rate (diqmax). It is a project-dependent parameter.
    tg: Time constant (Tg) (>= 0). It is a type-dependent parameter.
    WindTurbineType4aIEC: Wind turbine type 4A model with which this wind generator type 4 model is associated.
    WindTurbineType4bIEC: Wind turbine type 4B model with which this wind generator type 4 model is associated.
    """

    dipmax: float = 0.0  # Type #PU in CIM
    diqmin: float = 0.0  # Type #PU in CIM
    diqmax: float = 0.0  # Type #PU in CIM
    tg: int = 0  # Type #Seconds in CIM
    # *Association not used*
    # WindTurbineType4aIEC : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # WindTurbineType4bIEC : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindGenType4IEC"]
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
            "dipmax": [
                Profile.DY.value,
            ],
            "diqmin": [
                Profile.DY.value,
            ],
            "diqmax": [
                Profile.DY.value,
            ],
            "tg": [
                Profile.DY.value,
            ],
            "WindTurbineType4aIEC": [
                Profile.DY.value,
            ],
            "WindTurbineType4bIEC": [
                Profile.DY.value,
            ],
        }
