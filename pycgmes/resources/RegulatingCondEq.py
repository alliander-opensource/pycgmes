"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .EnergyConnection import EnergyConnection


@dataclass
class RegulatingCondEq(EnergyConnection):
    """
    A type of conducting equipment that can regulate a quantity (i.e. voltage or flow) at a specific point in the
      network.

    RegulatingControl: The regulating control scheme in which this equipment participates.
    controlEnabled: Specifies the regulation status of the equipment.  True is regulating, false is not regulating.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    RegulatingControl: Optional[str] = None  # Type M:0..1 in CIM
    controlEnabled: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=RegulatingCondEq\n"
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
                self.profiles.SSH.value,
                self.profiles.DY.value,
            ],
            # Attributes
            "RegulatingControl": [
                self.profiles.EQ.value,
            ],
            "controlEnabled": [
                self.profiles.SSH.value,
            ],
        }
