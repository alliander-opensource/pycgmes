"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .Connector import Connector


@dataclass
class BusbarSection(Connector):
    """
    A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment
      within a single substation.  Voltage measurements are typically obtained from voltage transformers that are
      connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled
      with exactly one logical terminal.

    ipMax: Maximum allowable peak short-circuit current of busbar (Ipmax in IEC 60909-0).  Mechanical limit of the
      busbar in the substation itself. Used for short circuit data exchange according to IEC 60909.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ipMax: float = 0.0  # Type #CurrentFlow in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=BusbarSection\n"
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
                self.profiles.SC.value,
            ],
            # Attributes
            "ipMax": [
                self.profiles.SC.value,
            ],
        }
