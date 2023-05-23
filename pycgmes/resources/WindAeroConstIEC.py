"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
class WindAeroConstIEC(IdentifiedObject):
    """
    Constant aerodynamic torque model which assumes that the aerodynamic torque is constant. Reference: IEC
      61400-27-1:2015, 5.6.1.1.

    WindGenTurbineType1aIEC: Wind turbine type 1A model with which this wind aerodynamic model is associated.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # WindGenTurbineType1aIEC : Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindAeroConstIEC\n"
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
            "WindGenTurbineType1aIEC": [
                self.profiles.DY.value,
            ],
        }
