"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
class WindContPType4aIEC(IdentifiedObject):
    """
    P control model type 4A. Reference: IEC 61400-27-1:2015, 5.6.5.5.

    dpmaxp4a: Maximum wind turbine power ramp rate (dpmaxp4A). It is a project-dependent parameter.
    tpordp4a: Time constant in power order lag (Tpordp4A) (>= 0). It is a type-dependent parameter.
    tufiltp4a: Voltage measurement filter time constant (Tufiltp4A) (>= 0). It is a type-dependent parameter.
    WindTurbineType4aIEC: Wind turbine type 4A model with which this wind control P type 4A model is associated.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    dpmaxp4a: float = 0.0  # Type #PU in CIM
    tpordp4a: int = 0  # Type #Seconds in CIM
    tufiltp4a: int = 0  # Type #Seconds in CIM
    # *Association not used*
    # WindTurbineType4aIEC : Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindContPType4aIEC\n"
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
            "dpmaxp4a": [
                self.profiles.DY.value,
            ],
            "tpordp4a": [
                self.profiles.DY.value,
            ],
            "tufiltp4a": [
                self.profiles.DY.value,
            ],
            "WindTurbineType4aIEC": [
                self.profiles.DY.value,
            ],
        }
