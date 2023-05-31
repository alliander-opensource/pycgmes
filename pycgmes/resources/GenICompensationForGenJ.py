"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
class GenICompensationForGenJ(IdentifiedObject):
    """
    Resistive and reactive components of compensation for generator associated with IEEE type 2 voltage compensator for
      current flow out of another generator in the interconnection.

    SynchronousMachineDynamics: Standard synchronous machine out of which current flow is being compensated for.
    VcompIEEEType2: The standard IEEE type 2 voltage compensator of this compensation.
    rcij: Resistive component of compensation of generator associated with this IEEE type 2 voltage compensator for
      current flow out of another generator (Rcij).
    xcij: Reactive component of compensation of generator associated with this IEEE type 2 voltage compensator for
      current flow out of another generator (Xcij).
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    SynchronousMachineDynamics: Optional[str] = None  # Type M:1 in CIM
    VcompIEEEType2: Optional[str] = None  # Type M:1 in CIM
    rcij: float = 0.0  # Type #PU in CIM
    xcij: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=GenICompensationForGenJ\n"
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
                self.profiles.DY.value,
            ],
            # Attributes
            "SynchronousMachineDynamics": [
                self.profiles.DY.value,
            ],
            "VcompIEEEType2": [
                self.profiles.DY.value,
            ],
            "rcij": [
                self.profiles.DY.value,
            ],
            "xcij": [
                self.profiles.DY.value,
            ],
        }
