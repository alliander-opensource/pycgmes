"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .AuxiliaryEquipment import AuxiliaryEquipment


@dataclass
class FaultIndicator(AuxiliaryEquipment):
    """
    A FaultIndicator is typically only an indicator (which may or may not be remotely monitored), and not a piece of
      equipment that actually initiates a protection event. It is used for FLISR (Fault Location, Isolation and
      Restoration) purposes, assisting with the dispatch of crews to "most likely" part of the network (i.e. assists
      with determining circuit section where the fault most likely happened).

    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # No attributes defined for this class.

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=FaultIndicator\n"
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
        }
