"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
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

    SynchronousMachineDynamics: Optional[str] = None  # Type M:1 in CIM
    VcompIEEEType2: Optional[str] = None  # Type M:1 in CIM
    rcij: float = 0.0  # Type #PU in CIM
    xcij: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GenICompensationForGenJ"]
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
                Profile.DY.value,
            ],
            # Attributes
            "SynchronousMachineDynamics": [
                Profile.DY.value,
            ],
            "VcompIEEEType2": [
                Profile.DY.value,
            ],
            "rcij": [
                Profile.DY.value,
            ],
            "xcij": [
                Profile.DY.value,
            ],
        }
