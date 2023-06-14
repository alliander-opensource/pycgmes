"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .HVDCDynamics import HVDCDynamics


@dataclass(config=DataclassConfig)
class VSCDynamics(HVDCDynamics):
    """
    VSC function block whose behaviour is described by reference to a standard model or by definition of a user-defined
      model.

    VsConverter: Voltage source converter to which voltage source converter dynamics model applies.
    """

    VsConverter: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=VSCDynamics"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "VsConverter": [
                Profile.DY.value,
            ],
        }
