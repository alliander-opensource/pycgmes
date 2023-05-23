"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
class WindContPType4bIEC(IdentifiedObject):
    """
    P control model type 4B. Reference: IEC 61400-27-1:2015, 5.6.5.6.

    dpmaxp4b: Maximum wind turbine power ramp rate (dpmaxp4B). It is a project-dependent parameter.
    tpaero: Time constant in aerodynamic power response (Tpaero) (>= 0). It is a type-dependent parameter.
    tpordp4b: Time constant in power order lag (Tpordp4B) (>= 0). It is a type-dependent parameter.
    tufiltp4b: Voltage measurement filter time constant (Tufiltp4B) (>= 0). It is a type-dependent parameter.
    WindTurbineType4bIEC: Wind turbine type 4B model with which this wind control P type 4B model is associated.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    dpmaxp4b: float = 0.0  # Type #PU in CIM
    tpaero: int = 0  # Type #Seconds in CIM
    tpordp4b: int = 0  # Type #Seconds in CIM
    tufiltp4b: int = 0  # Type #Seconds in CIM
    # *Association not used*
    # WindTurbineType4bIEC : Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindContPType4bIEC\n"
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
            "dpmaxp4b": [
                self.profiles.DY.value,
            ],
            "tpaero": [
                self.profiles.DY.value,
            ],
            "tpordp4b": [
                self.profiles.DY.value,
            ],
            "tufiltp4b": [
                self.profiles.DY.value,
            ],
            "WindTurbineType4bIEC": [
                self.profiles.DY.value,
            ],
        }
