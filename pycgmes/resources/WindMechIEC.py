"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindMechIEC(IdentifiedObject):
    """
    Two mass model. Reference: IEC 61400-27-1:2015, 5.6.2.1.

    cdrt: Drive train damping (cdrt). It is a type-dependent parameter.
    hgen: Inertia constant of generator (Hgen) (>= 0). It is a type-dependent parameter.
    hwtr: Inertia constant of wind turbine rotor (HWTR) (>= 0). It is a type-dependent parameter.
    kdrt: Drive train stiffness (kdrt). It is a type-dependent parameter.
    WindTurbineType3IEC: Wind turbine type 3 model with which this wind mechanical model is associated.
    WindTurbineType1or2IEC: Wind generator type 1 or type 2 model with which this wind mechanical model is associated.
    WindTurbineType4bIEC: Wind turbine type 4B model with which this wind mechanical model is associated.
    """

    cdrt: float = 0.0  # Type #PU in CIM
    hgen: int = 0  # Type #Seconds in CIM
    hwtr: int = 0  # Type #Seconds in CIM
    kdrt: float = 0.0  # Type #PU in CIM
    # *Association not used*
    # WindTurbineType3IEC : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # WindTurbineType1or2IEC : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # WindTurbineType4bIEC : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindMechIEC"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "cdrt": [
                Profile.DY.value,
            ],
            "hgen": [
                Profile.DY.value,
            ],
            "hwtr": [
                Profile.DY.value,
            ],
            "kdrt": [
                Profile.DY.value,
            ],
            "WindTurbineType3IEC": [
                Profile.DY.value,
            ],
            "WindTurbineType1or2IEC": [
                Profile.DY.value,
            ],
            "WindTurbineType4bIEC": [
                Profile.DY.value,
            ],
        }
