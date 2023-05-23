"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .DCBaseTerminal import DCBaseTerminal


@dataclass
class ACDCConverterDCTerminal(DCBaseTerminal):
    """
    A DC electrical connection point at the AC/DC converter. The AC/DC converter is electrically connected also to the
      AC side. The AC connection is inherited from the AC conducting equipment in the same way as any other AC
      equipment. The AC/DC converter DC terminal is separate from generic DC terminal to restrict the connection
      with the AC side to AC/DC converter and so that no other DC conducting equipment can be connected to the AC
      side.

    DCConductingEquipment: A DC converter terminal belong to an DC converter.
    polarity: Represents the normal network polarity condition. Depending on the converter configuration the value shall
      be set as follows: - For a monopole with two converter terminals use DCPolarityKind `positive` and
      `negative`. - For a bi-pole or symmetric monopole with three converter terminals use DCPolarityKind
      `positive`, `middle` and `negative`.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    DCConductingEquipment: Optional[str] = None  # Type M:1 in CIM
    polarity: Optional[str] = None  # Type M:1..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ACDCConverterDCTerminal\n"
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
                self.profiles.TP.value,
                self.profiles.EQ.value,
                self.profiles.SSH.value,
            ],
            # Attributes
            "DCConductingEquipment": [
                self.profiles.EQ.value,
            ],
            "polarity": [
                self.profiles.EQ.value,
            ],
        }
