"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .RegulatingControl import RegulatingControl


@dataclass
class TapChangerControl(RegulatingControl):
    """
    Describes behaviour specific to tap changers, e.g. how the voltage at the end of a line varies with the load level
      and compensation of the voltage drop by tap adjustment.

    TapChanger: The tap changers that participates in this regulating tap control scheme.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # TapChanger : list = field(default_factory=list)  # Type M:1..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=TapChangerControl\n"
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
            "TapChanger": [
                self.profiles.EQ.value,
            ],
        }
