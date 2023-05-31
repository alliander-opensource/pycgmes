"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
class EnergyArea(IdentifiedObject):
    """
    Describes an area having energy production or consumption.  Specializations are intended to support the load
      allocation function as typically required in energy management systems or planning studies to allocate
      hypothesized load levels to individual load points for power flow analysis.  Often the energy area can be
      linked to both measured and forecast load levels.

    ControlArea: The control area specification that is used for the load forecast.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # ControlArea : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=EnergyArea\n"
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
            ],
            # Attributes
            "ControlArea": [
                self.profiles.EQ.value,
            ],
        }
