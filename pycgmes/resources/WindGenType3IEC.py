"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
class WindGenType3IEC(IdentifiedObject):
    """
    Parent class supporting relationships to IEC wind turbines type 3 generator models of IEC type 3A and 3B.

    dipmax: Maximum active current ramp rate (dipmax). It is a project-dependent parameter.
    diqmax: Maximum reactive current ramp rate (diqmax). It is a project-dependent parameter.
    xs: Electromagnetic transient reactance (xS). It is a type-dependent parameter.
    WindTurbineType3IEC: Wind turbine type 3 model with which this wind generator type 3 is associated.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    dipmax: float = 0.0  # Type #PU in CIM
    diqmax: float = 0.0  # Type #PU in CIM
    xs: float = 0.0  # Type #PU in CIM
    # *Association not used*
    # WindTurbineType3IEC : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindGenType3IEC\n"
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
            "diqmax": [
                self.profiles.DY.value,
            ],
            "xs": [
                self.profiles.DY.value,
            ],
            "WindTurbineType3IEC": [
                self.profiles.DY.value,
            ],
        }
