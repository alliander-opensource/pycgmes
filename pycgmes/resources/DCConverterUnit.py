"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .DCEquipmentContainer import DCEquipmentContainer


@dataclass
class DCConverterUnit(DCEquipmentContainer):
    """
    Indivisible operative unit comprising all equipment between the point of common coupling on the AC side and the
      point of common coupling - DC side, essentially one or more converters, together with one or more converter
      transformers, converter control equipment, essential protective and switching devices and auxiliaries, if any,
      used for conversion.

    operationMode: The operating mode of an HVDC bipole (bipolar, monopolar metallic return, etc).
    Substation: The containing substation of the DC converter unit.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    operationMode: Optional[str] = None  # Type M:1..1 in CIM
    Substation: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=DCConverterUnit\n"
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
            "operationMode": [
                self.profiles.EQ.value,
            ],
            "Substation": [
                self.profiles.EQ.value,
            ],
        }
