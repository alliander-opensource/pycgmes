"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=WindMechIEC\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.DY.value,
            ],
            # Attributes
            "cdrt": [
                self.profiles.DY.value,
            ],
            "hgen": [
                self.profiles.DY.value,
            ],
            "hwtr": [
                self.profiles.DY.value,
            ],
            "kdrt": [
                self.profiles.DY.value,
            ],
            "WindTurbineType3IEC": [
                self.profiles.DY.value,
            ],
            "WindTurbineType1or2IEC": [
                self.profiles.DY.value,
            ],
            "WindTurbineType4bIEC": [
                self.profiles.DY.value,
            ],
        }
