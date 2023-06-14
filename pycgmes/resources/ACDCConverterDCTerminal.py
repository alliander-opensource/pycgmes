"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DCBaseTerminal import DCBaseTerminal


@dataclass(config=DataclassConfig)
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

    DCConductingEquipment: Optional[str] = None  # Type M:1 in CIM
    polarity: Optional[str] = None  # Type M:1..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ACDCConverterDCTerminal"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.TP.value,
                Profile.EQ.value,
                Profile.SSH.value,
            ],
            # Attributes
            "DCConductingEquipment": [
                Profile.EQ.value,
            ],
            "polarity": [
                Profile.EQ.value,
            ],
        }
