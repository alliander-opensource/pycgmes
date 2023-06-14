"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TapChanger import TapChanger


@dataclass(config=DataclassConfig)
class PhaseTapChanger(TapChanger):
    """
    A transformer phase shifting tap model that controls the phase angle difference across the power transformer and
      potentially the active power flow through the power transformer.  This phase tap model may also impact the
      voltage magnitude.

    TransformerEnd: Transformer end to which this phase tap changer belongs.
    """

    TransformerEnd: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PhaseTapChanger"]
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
                Profile.EQ.value,
                Profile.SSH.value,
            ],
            # Attributes
            "TransformerEnd": [
                Profile.EQ.value,
            ],
        }
