"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
class WindContQLimIEC(IdentifiedObject):
    """
    Constant Q limitation model. Reference: IEC 61400-27-1:2015, 5.6.5.9.

    qmax: Maximum reactive power (qmax) (> WindContQLimIEC.qmin). It is a type-dependent parameter.
    qmin: Minimum reactive power (qmin) (< WindContQLimIEC.qmax). It is a type-dependent parameter.
    WindTurbineType3or4IEC: Wind generator type 3 or type 4 model with which this constant Q limitation model is
      associated.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    qmax: float = 0.0  # Type #PU in CIM
    qmin: float = 0.0  # Type #PU in CIM
    # *Association not used*
    # WindTurbineType3or4IEC : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindContQLimIEC\n"
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
            "qmax": [
                self.profiles.DY.value,
            ],
            "qmin": [
                self.profiles.DY.value,
            ],
            "WindTurbineType3or4IEC": [
                self.profiles.DY.value,
            ],
        }
