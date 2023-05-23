"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .OperationalLimit import OperationalLimit


@dataclass
class VoltageLimit(OperationalLimit):
    """
    Operational limit applied to voltage. The use of operational VoltageLimit is preferred instead of limits defined at
      VoltageLevel. The operational VoltageLimits are used, if present.

    normalValue: The normal limit on voltage. High or low limit nature of the limit depends upon the properties of the
      operational limit type. The attribute shall be a positive value or zero.
    value: Limit on voltage. High or low limit nature of the limit depends upon the properties of the operational limit
      type. The attribute shall be a positive value or zero.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    normalValue: float = 0.0  # Type #Voltage in CIM
    value: float = 0.0  # Type #Voltage in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=VoltageLimit\n"
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
                self.profiles.EQ.value,
                self.profiles.SSH.value,
            ],
            # Attributes
            "normalValue": [
                self.profiles.EQ.value,
            ],
            "value": [
                self.profiles.SSH.value,
            ],
        }
