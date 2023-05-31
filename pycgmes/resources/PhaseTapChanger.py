"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .TapChanger import TapChanger


@dataclass
class PhaseTapChanger(TapChanger):
    """
    A transformer phase shifting tap model that controls the phase angle difference across the power transformer and
      potentially the active power flow through the power transformer.  This phase tap model may also impact the
      voltage magnitude.

    TransformerEnd: Transformer end to which this phase tap changer belongs.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    TransformerEnd: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PhaseTapChanger\n"
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
            "TransformerEnd": [
                self.profiles.EQ.value,
            ],
        }
