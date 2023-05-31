"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=WindGenType4IEC\n"
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
            "dipmax": [
                self.profiles.DY.value,
            ],
            "diqmin": [
                self.profiles.DY.value,
            ],
            "diqmax": [
                self.profiles.DY.value,
            ],
            "tg": [
                self.profiles.DY.value,
            ],
            "WindTurbineType4aIEC": [
                self.profiles.DY.value,
            ],
            "WindTurbineType4bIEC": [
                self.profiles.DY.value,
            ],
        }
